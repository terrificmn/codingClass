(function() {

  // Define "global" variables
  var connectButton = null;
  var disconnectButton = null;
  var sendButton = null;
  var messageInputBox = null;
  var receiveBox = null;
  
  var localConnection = null;   // RTCPeerConnection for our "local" connection
  var remoteConnection = null;  // RTCPeerConnection for the "remote"
  
  var sendChannel = null;       // RTCDataChannel for the local (sender)
  var receiveChannel = null;    // RTCDataChannel for the remote (receiver)
  
  // Functions
  // Set things up, connect event listeners, etc.
  
  function startup() {
    console.log("startup!");
    connectButton = document.getElementById('connectButton');
    disconnectButton = document.getElementById('disconnectButton');
    sendButton = document.getElementById('sendButton');
    messageInputBox = document.getElementById('message');
    receiveBox = document.getElementById('receivebox');

    // Set event listeners for user interface widgets

    connectButton.addEventListener('click', connectPeers, false);
    disconnectButton.addEventListener('click', disconnectPeers, false);
    sendButton.addEventListener('click', sendMessage, false);
  }
  
  // Connect the two peers. Normally you look for and connect to a remote
  // machine here, but we're just connecting two local objects, so we can
  // bypass that step.
  
  function connectPeers() {
    // Create the local connection and its event listeners
    
    localConnection = new RTCPeerConnection();
    
    // Create the data channel and establish its event listeners
    sendChannel = localConnection.createDataChannel("sendChannel");
    sendChannel.onopen = handleSendChannelStatusChange;
    sendChannel.onclose = handleSendChannelStatusChange;
    
    // Create the remote connection and its event listeners
    
    remoteConnection = new RTCPeerConnection();
    remoteConnection.ondatachannel = receiveChannelCallback;
    
    // Set up the ICE candidates for the two peers
    
    localConnection.onicecandidate = e => !e.candidate
        || remoteConnection.addIceCandidate(e.candidate)
        .catch(handleAddCandidateError);

    remoteConnection.onicecandidate = e => !e.candidate
        || localConnection.addIceCandidate(e.candidate)
        .catch(handleAddCandidateError);
    
    // Now create an offer to connect; this starts the process
    
    localConnection.createOffer()  // SDP(Session Description Protocol) 만듬 - audio, video, 등을 설정도 가능
    .then(offer => localConnection.setLocalDescription(offer)) // the loical end of the connection
    .then(() => remoteConnection.setRemoteDescription(localConnection.localDescription))  // local peer를 remote peer와 연결 - remoteConnection 커넥션 정보를 알게 됨  // 실제는 여기에 signaling server가 필요하다고 함
    .then(() => remoteConnection.createAnswer()) //  remote peer가 응답하게 하는 것
    .then(answer => remoteConnection.setLocalDescription(answer)) // answer가 만들어지면 setLocalDescription로 전달. remote의 end of the connection 을 만들어줌
    .then(() => localConnection.setRemoteDescription(remoteConnection.localDescription)) // 마지막으로 localConnection 의 remote description이 설정됨
    .catch(handleCreateDescriptionError); // cath errors
  }
    
   // 실제로는 signalling server가 필요해서 서로 description을 교환하게 됨 
   // peer-to-peer 연결이 성공적으로 되면, RTCPeerConnection의 icecandiate 이벤트가 시작됨
   // 아래의 handleCreateDescriptionError, handleLocalAddCandidateSuccess, handleRemoteAddCandidateSuccess, handleAddCandidateError 에서 처리

  // Handle errors attempting to create a description;
  // this can happen both when creating an offer and when
  // creating an answer. In this simple example, we handle
  // both the same way.
  
  function handleCreateDescriptionError(error) {
    console.log("Unable to create an offer: " + error.toString());
  }
  
  // Handle successful addition of the ICE candidate
  // on the "local" end of the connection.
  // 연결되었을 경우 버튼을 disabled 해준다.
  function handleLocalAddCandidateSuccess() {
    connectButton.disabled = true;
  }

  // Handle successful addition of the ICE candidate
  // on the "remote" end of the connection.
  
  function handleRemoteAddCandidateSuccess() {
    disconnectButton.disabled = false;
  }

  // Handle an error that occurs during addition of ICE candidate.
  
  function handleAddCandidateError() {
    console.log("Oh noes! addICECandidate failed!");
  }

  // Handles clicks on the "Send" button by transmitting
  // a message to the remote peer.
  // send버튼을 눌리면 sendMessage() 호출, 버튼의 click()이벤트 , 메세지박스의 value를  senChannel에 보내고 input 박스를 비우고 커서를 focus 해줌
  function sendMessage() {
    var message = messageInputBox.value;
    sendChannel.send(message);
    
    // Clear the input box and re-focus it, so that we're
    // ready for the next message.
    
    messageInputBox.value = "";
    messageInputBox.focus();
  }
  
  // Handle status changes on the local end of the data
  // channel; this is the end doing the sending of data
  // in this example.
  /// local peer에서 open or close 이벤트가 발생하면 아래 함수 작동이 된다.
  function handleSendChannelStatusChange(event) {
    if (sendChannel) {
      var state = sendChannel.readyState;
      
      /// state가 'open' 이면 두 개의 peer 사이의 연결을 만드는 것이 끝났다는 의미가 된다.
      // 즉 html페이지의 버튼들의 상태가 변경된다.
      if (state === "open") {
        messageInputBox.disabled = false;
        messageInputBox.focus();
        sendButton.disabled = false;
        disconnectButton.disabled = false;
        connectButton.disabled = true;
        // 아래는 반대의 경우이고 state가 "closed" 일 경우에 해당
      } else {
        messageInputBox.disabled = true;
        sendButton.disabled = true;
        connectButton.disabled = false;
        disconnectButton.disabled = true;
      }
    }
  }
  
  // Called when the connection opens and the data
  // channel is ready to be connected to the remote.
  /// RTCPeerConnection가 열렸다면, datachannel 이벤트가 remote에 전송되는데 receiveChannelCallback 함수가 호출되게 된다.
  
  function receiveChannelCallback(event) {
    receiveChannel = event.channel;
    receiveChannel.onmessage = handleReceiveMessage;
    receiveChannel.onopen = handleReceiveChannelStatusChange;
    receiveChannel.onclose = handleReceiveChannelStatusChange;
  }
  
  // Handle onmessage events for the receiving channel.
  // These are the data messages sent by the sending channel.
  /// 데이터가 remote peer한테 받아질 경우 아래의 함수가 invoke 되며, "message"가 remote 채널에 발생했을 경우이다.
  function handleReceiveMessage(event) {
    var el = document.createElement("p");
    var txtNode = document.createTextNode(event.data);
    
    el.appendChild(txtNode);
    receiveBox.appendChild(el);
    /// 기초 DOM 삽입
    /// P 태그 (paragraph)를 만들고 txtNode에 text 데이터를 담고 event의 data (property)를 받게 된다.
    /// receiveBox 는 div 태그인 #receivebox 에 삽입
  }
  
  // Handle status changes on the receiver's channel. 
  // 채널의 상태가 connection state가 변경되면 아래 함수가 사용되는데, channel이 오픈되었을 경우와 닫혔을 경우에 발생
  /// remote 쪽에서는 event는 무시, log가 표시
  /// event 는 RTCDataChannelEvent. 
  function handleReceiveChannelStatusChange(event) {
    if (receiveChannel) {
      console.log("Receive channel's status has changed to " +
                  receiveChannel.readyState);
    }
    
    // Here you would do stuff that needs to be done
    // when the channel's status changes.
  }
  
  // Close the connection, including data channels if they're open.
  // Also update the UI to reflect the disconnected status.
  
  function disconnectPeers() {
  
    // Close the RTCDataChannels if they're open.
    
    sendChannel.close();
    receiveChannel.close();
    
    // Close the RTCPeerConnections
    
    localConnection.close();
    remoteConnection.close();

    sendChannel = null;
    receiveChannel = null;
    localConnection = null;
    remoteConnection = null;
    
    // Update user interface elements
    
    connectButton.disabled = false;
    disconnectButton.disabled = true;
    sendButton.disabled = true;
    
    messageInputBox.value = "";
    messageInputBox.disabled = true;
  }
  
  // Set up an event listener which will run the startup
  // function once the page is done loading.
  // 여기에서 'load' event listener를 셋업해서 페이지가 다 로드가 되면 startup() 를 호출하게 됨
  window.addEventListener('load', startup, false);
})();