# socket programming

[여기를 참고하자](https://www.geeksforgeeks.org/socket-programming-cc/)


| Server쪽의 Process 흐름   | - |    Client쪽 흐름 |
| --- | --- | --- |
| 1. socker()  | |                  1. socket() |
| 2. bind()    | |                  2.  connect() |
| 3. listen() | | |
| 4. accept() | | |
| read()  | | write() |
| write() | | read()  |

