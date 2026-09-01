설치방식이 홈피에서 rpm파일을 제공하던것이 바뀌었다
dnf, snap도 가능

커맨드로 등록 및 다운
RHEL, Fedora, and CentOS based distributions#

We currently ship the stable 64-bit VS Code in a yum repository, the following script will install the key and repository:
```
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
```

Then update the package cache and install the package using dnf (Fedora 22 and above):
```
dnf check-update
sudo dnf install code
```
Or on older versions using yum:
```
yum check-update
sudo yum install code
```
Due to the manual signing process and the system we use to publish, the yum repo may lag behind and not get the latest version of VS Code immediately.

