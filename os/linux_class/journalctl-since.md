# journalctl
since & until 사용하기   
시간대를 특정해서 볼 수 있음 

`--since "18:40:00" --until "19:05:00"`  since 만 사용해도 가능  


날짜 까지 적용하려면  `--since "2026-06-25 18:40:00"`
  
mosquitto 등에서는 시간 로그를 활성화 했다면은 특정 시간대의 로그만 보는 식으로 활용이 가능하다 


이런식도 가능하다고 하는데 해보지는 못함  
`journalctl --since "1 hour ago" --until "30 minutes ago"`


