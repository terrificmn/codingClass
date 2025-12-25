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


