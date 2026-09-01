## CentOS 8 최초 설치 할 때 권장 프로그램 사용하기
usb로 부팅한 후 인스톨 화면까지는 잘 넘어가는데   
base repository 셋팅을 못하고 에러가 발생할 때  

error setting up base repository 일때   

원인은 :   
부팅가능 usb를 만들 때 인터넷에서 흔히 추천하는 rufus-3 프로그램을 이용했는데   
계속 같은 에러가 발생해서 알아보니

공식 매뉴얼에서 권장하는 프로그램으로 설치 후 해결   

FedoraMediaWriter-win64-4.2 버전을 받아서   
다운로드: https://github.com/FedoraQt/MediaWriter/releases   
iso파일로 굽기 시도   

참고 사이트: https://docs.centos.org/en-US/centos/install-guide/Making_Media_USB_Windows/