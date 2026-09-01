# git config 에서 id 바꾸기

리드 only 계정으로 클론을 받은 후에   
해당 아이디로는 push를 할 수가 없다.  

간단하게 
cd .git
로 이동 후에 config 파일을 열어준다.  

[remote "origin"]   
부분을 수정해주는데 url 에 아이디가 결합되어 있다면   
예 http://myuser@github.com/repo_url/repo.git   
으로 되어 있는 부분에서 아이디를 빼주고 저장해 준다.

global로 user가 등록이 되어 있으면 user을 따로 등록 안해도 되고   
만약 local로 해당 패키지에만 user을 등록하려면 

[user]  
    name = "myid"
    email = "myemail@email.com"

처럼 등록 해주면 된다.   

이제 해당 유저의 token 만 유효하다면 remote origin 으로 push 가 가능해진다

