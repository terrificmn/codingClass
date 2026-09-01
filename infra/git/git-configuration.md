Git 환경 설정 및 명령어 사용

깃허브 처음 리포지터리 만들고 첫 add, commit, push 까지 하기
echo "# myBlogProject" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add myblog https://github.com/terrificmn/myBlogProject.git
git push -u myblog main
헛깔리까봐 remote를 orgin 대신에 myblog로 해서 등록함 
기존에 공부하는 깃허브는 origin이어서 괜히 착각할 것 같아서 

**설명: 
  git branch -M main 는 oldbranch명을 바꾸는 것 아마도 master에서 main으로

*새로운 리포지터리 만듬 (08Mar, 2021)
-u 옵션이랑


vscode 열기 (자동으로 열림)
  $code .

help옵션 사용하기
$git 명령어 --help
그러면 매뉴얼 페이지가 브라우저로 열린다


에디터 등록하기, 여기서 --global 옵션을 주어서 editor 선택
  $git config --global core.editor "code --wait"
또는 
  $git config --global core.editor "code"

vim 또는 vi를 등록하는 경우  
git config --global core.editor "vim"


**참고: 
예를 들어, "code --wait"은 vscode 의미하고, "atom --wait"는 아톰 에디터임

***참고: --wait의 차이점은 git config파일을 열어 볼려고 할 때 
vscode에디터에서 환경설정 파일이 열리고 터미널에서 또 작업을 할 수 있으나 
--wait 옵션을 주면 환경설정 파일이 저장을 하고 끄기전에는 터미널에서 작업을 할 수 없음 (즉, 터미널이 wait중)
--wait 옵션을 추천!

코드에디터로 환경설정 파일 열기
  $git config --global -e

이름과 이메일 등록
  $git config --global user.name "Your Name"
  $git config --global user.email "youremail@domain.com"

configuration 확인
  $git config --list
또는 
  $git config --global --list

리눅스는 input으로 설정
  $git config --global core.autocrlf input
또는 윈도우는 true로 설정
  $git config --global core.autocrlf true

**참고: core.autocrlf 줄바꿈이 일어날 때 
윈도우에서는 text \r\n (carriage-return)과 (new line feed) 일어나는 데 (줄바꿈할 때)
리눅스나 맥에서는 text \n (carriage-return)이 발생하지 않고 (new line feed)만 되므로 
윈도우와 리눅스에 서로 작업할 때 core.autocrlf 에서 자동으로 윈도우에서 저장할 때는 \r\n을 해주고
맥이나 리눅스에서는 \n 해준다고 함

리눅스는 input , 윈도우에서는 true로 설정해줘야지,
윈도우에서 작업했을 때와 리눅스에서 했을 때 서로 문제가 없도록 해준다고 함

한글파일명이 354\213\234\354\236\221.txt 이런식으로 나올 때 설정해주기

  $git config --global core.quotepath false

**참고: "" \ \t \n \\ 항상 escape 되어 지는데 
한글 인코딩이 utf-8에 들어가서 큰 바이트를 가지면 unsual 상태로 바뀌게 되어서 그렇다고 함
기본값인 true에서 false로 바꾸면 0x80보다 크더라도 unsual상태로 안된다고 함
뭐.. 그렇다고 함......


remote (원격 저장소) 연결하기
  $git remote add origin https://github.com/(본인계정or계정)/(repository_name)coding.git

이렇게 origin으로 한번 저장해놓으면 다음부터는 origin만 사용해서 remote에 접속해진다

등록한 원격저장소 지우기
  $git remote remove origin


