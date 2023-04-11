유저 만들 때 사용하거나. 뒤의 문자열이 패스워드가 된다    

```
RUN echo 'root:Docker!' | chpasswd  
```
또는   
```
RUN echo 'Docker!' | passwd --stdin root   
```

docker는 root권한으로 build를 하는데 일반 유저로 하려고 하면  (먼저 유저를 만들기는 해야함)
sudo등을 할 때 비번을 쳐야하는데 build 하는 경우네는 입력을 할 수가 없음   

> 빌드 완료 후 exec, run 등으로 tty로 하는 것은 얼마든지 가능  


일반 유저로 sudo 사용할 때 비번 넘겨주기  
```
echo "pass" | sudo -S apt update
```
예:
```
RUN echo "user" | sudo -S chmod 777 /home
```

비번이 노출이 되므로 적절히 사용해야할 듯 하다  


