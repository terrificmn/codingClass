# boost socket

[최신 튜토리얼 소켓](https://www.boost.org/doc/libs/1_81_0/doc/html/boost_asio/tutorial.html)

tcp 관련 / 







> 부스트 예제에서 daytime 같은 경우에는    
> daytime 같은 경우에는 서비스 네임이 된다고 함. 이미 정해져 있는 프로토콜

boost 쿼리를 이용해서 바꿀 수 있다고 하는 듯 함


Daytime is simply another protocol (like FTP, etc) and it uses port 13. If you want to connect to the server on a specific port number, then your code would look like this:

tcp::resolver::query query(host_ip, "5678"); // 5678 is the port number

 [query 관련 여기에 document 확인](https://www.boost.org/doc/libs/1_48_0/doc/html/boost_asio/reference/ip__basic_resolver_query/basic_resolver_query/overload3.html)

