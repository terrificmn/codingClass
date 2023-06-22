# webrtc 의 STUN 과 ICE  
webRTC 에서 NAT에서 port 설정을 할 필요가 없게 그 port 관련해서  
STUN과 ICE 란 놈들이 port를 동적으로 (dynamically) 포트를 열어주게 된다   

stack overflow에서의 가져온 내용  

Here's how it works (in a really brief description).

    Client opens a socket on a random port (e.g. 50001)

    Contacts STUN server using that socket to discover the external IP:port mapping for this socket. (e.g. 192.168.1.2:50001 maps to 1.2.3.4:50001). Ports don't necessarily have to match between internal and external addresses, but they usually do, so I'll keep with that for this example.

    Through an external mechanism (SIP, XMPP, Jingle, cups with strings), the candidate address list of both nodes are exchanged. This includes all known internal and external addresses collected (e.g. 192.168.1.2:50001 and 1.2.3.4:50001).

    Using the same socket opened in step 1, both sides send (STUN) messages (UDP packets) directly between each other. The first pair of messages may be blocked by the router/firewall. But because one side initiated an outbound packet to the remote address, subsequent packets from that address are allowed back in. This is called the "hole punching step". Hence, the port is dynamically open without the router needing any specific configuration.

