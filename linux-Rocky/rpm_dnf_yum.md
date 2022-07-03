# rpm dnf yum 비교
rpm dnf yum 비교

## rpm
**참고 자료: rpm으로 설치 시 (RedHat Package Manager)   
  RPM is free and released under GPL (General Public License).   
  RPM keeps the information of all the installed packages under /var/lib/rpm database.   
  RPM is the only way to install packages under Linux systems, if you’ve installed packages using source code, then rpm won’t manage it.   
  RPM deals with .rpm files, which contains the actual information about the packages such as: what it is, from where it comes, dependencies info, version info etc.  

rpm 명령어 옵션 설명   
-i : install a package   
-v: verbose for a nicer display   
-h: print hash marks as the package archive is unpacked   

즉, 레드햇 리눅스 계열, CentOs, Fedora 등에서 프로그램 설치할 때 사용하지만 의존성 문제는 자동으로 해결해 주지 않아서    
사용자가 찾아서 해결해야하는 것으로 알고 있음.      




## dnf 와 yum
rpm과 다르게 yum, dnf 등은 repository를 가지고 있어서 관련 의존성은 어느정도 해결해준다.    

**참고: dnf와 yum   
We will be using the open-source package manager tool DNF,   
which stands for Dandified YUM the next-generation version of the Yellowdog Updater, Modified (that is, yum).   
DNF is a package manager that is now the default package manager for Red Hat based Linux systems like CentOS.   
It will let you install, update, and remove software packages on your server.  

아무래도 dnf가 최신이므로 dnf를 적극 사용하자

