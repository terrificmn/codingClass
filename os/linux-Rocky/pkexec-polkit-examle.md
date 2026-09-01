# pkexec 
under  `/etc/polkit-1/rules.d/`  
파일을 하나 만들어 준다.  *45-pkexec-keep.rules*  
sudo vi 위의 경로로 만들거나, 아예 root로 로그인해야함. cd나, 파일 확인할 수 있는 권한이 없다.  

> fedora의 경우  
그룹이 polkitd 임  
아마도 그룹에 현재 사용자를 넣어주면 sudo로도 가능할 듯 하다. (해보지는 못함)  

내용은 아래처럼 만들어 주면 된다.

```
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.policykit.exec" &&
        subject.user == "myuser") {
	action.message = "Authentication required for system operation";
        return polkit.Result.AUTH_ADMIN_KEEP;
    }
});
```

이렇게 해주면 auth가 인증되면 다시 패스워드를 물어보지 않는다.  


## ubuntu
강제로 룰 바꿔버리기  
ubuntu에서는 fedora 처럼 rule 추가해서 하는것이 안된다.  
여러방법으로 시도했지만 다 실패  

직접 action_id 부분은 xml을 변경해서 사용하면 일단은 가능하다

sudo vi /usr/share/polkit-1/actions/org.freedesktop.policykit.policy

여기에서 action id="org.freedesktop.polickit.exec" 으로 되어 있는 태그의
이하의 defaults 에 있는 태그를 수정해준다.
이 중 allow_active 를 auth_admin 에서 auth_admin_keep 로 변경 해주면 됨

 <defaults>
      <allow_any>auth_admin</allow_any>
      <allow_inactive>auth_admin</allow_inactive>
      <allow_active>auth_admin_keep</allow_active>
    </defaults>

이후 재부팅후 pkexec echo hello 로 해서 비번 입력 후
다시 한번 실행했을 때 비번을 안 물어보면 성공

일단 TODO: auto_udevrule_app 에서는 실패함.. bash 길게 이어지는
프롬프트가 문제가 될 가능성이 있을 지도 모름.
그래서 temporary 로 처리가 되어 일지도..




다만, Unbuntu 22 에서는 정책이 달라서 위의 javascript 만으로는 안 되고 아예 설정파일을 만들어야 한다. 

1차 시도.
강제로 룰 바꿔버리기
ubuntu에서는 fedora 처럼 rule 추가해서 하는것이 안된다. 
여러방법으로 시도했지만 다 실패

직접 action_id 부분은 xml을 변경해서 사용하면 일단은 가능하다 
sudo vi /usr/share/polkit-1/actions/org.freedesktop.policykit.policy 

여기에서 action id="org.freedesktop.polickit.exec" 으로 되어 있는 태그의 
이하의 defaults 에 있는 태그를 수정해준다. 
이 중 allow_active 를 auth_admin 에서 auth_admin_keep 로 변경 해주면 됨
 
 <defaults>
      <allow_any>auth_admin</allow_any>
      <allow_inactive>auth_admin</allow_inactive>
      <allow_active>auth_admin_keep</allow_active>
    </defaults>

이후 재부팅후 pkexec echo hello 로 해서 비번 입력 후 
다시 한번 실행했을 때 비번을 안 물어보면 성공

일단 TODO: auto_udevrule_app 에서는 실패함.. bash 길게 이어지는 
프롬프트가 문제가 될 가능성이 있을 지도 모름. 
그래서 temporary 로 처리가 되어 일지도..



---- 
두 번째 시도

12월 11 21:52:40 sgtubunmsi gnome-shell[12697]: polkitAuthenticationAgent: Received 2 identities that can be used for authentication. Only considering one.
12월 11 21:52:44 sgtubunmsi polkitd(authority=local)[14118]: Operator of unix-session:15 successfully authenticated as unix-user:amrrobot to gain TEMPORARY authorization for action org.freedesktop.policykit.exec for unix-process:30246:1270054 [sh -c pkexec bash -c "dmesg | grep ttyACM"] (owned by unix-user:amrrobot)
12월 11 21:52:44 sgtubunmsi pkexec[30247]: pam_unix(polkit-1:session): session opened for user root(uid=0) by (uid=1001)


의심되는 부분

sh 커맨드로 쌓여있다. 실행하는 유저가 다르다, 등... 둘다 하나씩 해결
sudo usdermod -aG sudo $USER

감시하려면

sudo journalctl -f | grep -i polkit

journalctl -f | grep -i "polkit\|pkexec\|authentication"




파일을 만든다.

/etc/polkit-1/localauthority/50-local.d/pkexec-keep-session.pkla 

우분투 22에서는 관련 보안이 높은 듯 하다. 유저로 접근이 불가능하고 
root로 접속해야한다.  
sudo passwd 로 비번을 변경하고, (첫 시도시).. 주의할 점은 당연하겠지만 까먹으면 안됨




[Allow pkexec to keep session]
Identity=unix-user:amrrobot
Action=org.freedesktop.policykit.exec
ResultActive=auth_admin_keep
ResultInactive=auth_admin_keep
ResultAny=auth_admin_keep


user를 전체다 할려면 Identity=unix-user:*
아래의 auth_admin_keep 를 yes 로 바꾸게 되면 비번을 전혀 안 물어보게 된다. 
이후 파일 권한을 -rw-r--r-- 로 바꾼다. 아마 655 ?


나머지는 클로드 참고해서 정리!

간단하게 터미널에서 테스트
pkexec bash -c 'dmesg | grep tty'
pkexec bash -c 'echo "test 2"'

두 번째 echo 커맨드 시 비번을 안 물어보면 성공,


여기에서 더 중요한 것은 GUI app에서 popen 을 이용하게 되면 결국 sh -c 형태로 wrapper 형태로 사용이 되게 된다. 
위의 예제 처럼 bash -c 로만 사용하면 cache 하는데 문제가 없지만,  

sh -c 형태로 감싸지면 결국 temporary 로 사용이 되게 되어서 계속 패스워드를 물어보게 된다.  

그래서 fork 형태를 사용하는 방법으로 코드를 바꾸면 pkexec bash -c 같은 형태로만 실행이 되어서 인증 캐쉬에 문제가 없어짐
>>> 이와 관련해서 정리하기!

