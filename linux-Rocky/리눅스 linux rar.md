# 리눅스 rar 설치
압축파일을 rar을 풀기위해서는 rar을 설치해줘야하는데
CentOS repository에는 없는 듯 하다..

웹사이트에서 리눅스용 X64버전으로 다운을 받자~ wget으로 받을려고 했지만 
인터넷으로 나와있는 링크가 작동을 안하는 듯

다른 버전으로 wget 
```
$wget -v https://www.rarlab.com/rar/rarlinux-x64-6.0.2b1.tar.gz
```
또는 
[rarlab 에서 다운로드](https://www.rarlab.com/download.htm)


```
$tar zxvf rarlinux-x64-6.0.2b1.tar.gz
```
그러면 rar 디렉토리에 풀려있는데
rar, unrar 2개의 파일을 복사해주면 된다


```
sudo cp -v rar unrar /usr/local/bin/
```
(-v 옵션은 보기 옵션임)

이제 rar을 입력해보면 명령어 리스트가 나오는데 이 중 당장 필요한 것은 2개정도

```
e             Extract files without archived paths
x             Extract files with full path
```
그래서 대충 조합하면

```
$rar e rarzipfile.rar
```
안에 있는 압축된 파일들이 한 디렉토리에 모여있는게 아니라면 현재 디렉토리에 다 풀리게 되므로 주의
(디렉토리를 하나 만들어서 이동해준다음에 압축푸는것이 좋을 듯하다)