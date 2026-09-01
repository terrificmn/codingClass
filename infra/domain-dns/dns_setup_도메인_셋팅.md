1. 먼저 도메인 네임을 구입해야한다  
먼저 공짜로 되는 지 알았다...;;;
공짜가 있기는 하다 Freenom
namecheap, 등..

2. 도메인 이름을 linode의 도메인 네임서버로 셋팅   
도메인을 구입한 곳에서 Domain List 에서 NameServers 셋팅에서 DNS를   
Lionode의 네임으로 변경해준다   
```
ns1.linode.com
ns2.linode.com
ns3.linode.com
ns4.linode.com
ns5.linode.com
```

24시간에서 최대 48시간 걸릴 수 있다고 한다.   
사실상 50분 정도 걸린듯 하다

3. Linodes로 로그인을 한 후에
Domains 메뉴에서 create를 해줘야한다 
스샷 참고

### A/AAAA Record 
Hostname 설정 
subdomain 이름인 qspblog.com 을 지칭하거나 새로운 이름을 해줄 수 있다.  
그냥 그대로 둠   
IP address는 IPv6,  (quad A 라고 부르는 AAAA를 만들어 주는데 이게 들어가 있음.   
IPv4 도 입력하게 되어 있는데 기본적으로 만들어준다

TTL은 default가 24시간으로 되어 있다고 한다.  ... 버튼을 눌러 EDIT를 눌러서   
5분으로 바꿈

