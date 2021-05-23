# openmediavault 를 사용해서 NAS 서버 만들기

[openmediavault 사이트를 참고](https://www.openmediavault.org/)

라즈베리파이를 NAS 서버로 사용하려면 openmediavault 를 설치를 해줘야한다.

추천은 사이트를 들어가면 ISO 이미지 파일을 제공하는데, ARM 을 위해서 
X86 아키텍쳐로 미리 설정들이 되어 있는 이미지 라고 함.
 
아예 ISO 파일을 다운받아서 Etcher 등으로 MicroSD 카드에 복사시켜서 사용하는 것을 추천!

Etcher 프로그램이 잘 안 된다면 리눅스 dd 명령어로 카피할 수 있음

<a href="#">dd명령어 설치 보러가기 - 업데이트 예정 </a>

<br>

# openmediavault 를 Debian에서 사용할 수 있게 설치하기
확인되지는 않았지만 (버그 인지는 모르겠지만) 설치 후에 유선랜/무선랜을 사용할 수 없는 상태가 됨  
그래서.. 처음부터 **ISO이미지로 하는 것을 추천~** 

그래도 설치되어 있는 라즈베리 파이에 설치할 경우에는 아래처럼 한다  
먼저 apache2 서버가 작동하고 있다면 멈춰준다.  
```
systemctl status apache2
```
만약 작동중이라면 중지 시켜준다. 
```
systemctl stop apache2
systemctl disable apache2
```

주의 할점은 먼저 데비안 계열에서도 Raspberry PI 는 위의 공식 매뉴얼(사이트)에 나온 것의 부분만 되므로,   
중요! 전용 깃허브 installation script를 사용해서 설치를 해야한다  

[깃허브 인스톨 사용하기](https://github.com/OpenMediaVault-Plugin-Developers/installScript)

위의 페이지에서 wget이나 curl로 설치하는 방법이 있는데.. 그 중 하나 선택 해서 설치하면 됨
```shell
$sudo wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash
```

이제 설치 스크립트가 실행이 되면서 실행이 된다.

자동으로 재부팅이 되고 나면 웹브라우저를 열고   
localhost를 입력하면  

아이디 admin  
비번 openmediavalut 

Nas를 사용할 수 있다.

<a href="#"> openmediavalut 무선랜이 안잡히는 경우 트러블 슈팅 보러가기 </a>




