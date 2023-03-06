
업데이트 필요!!!!!!!!!

실패 시
Certbot failed to authenticate some domains (authenticator: webroot). The Certificate Authority reported these problems:
  Domain: qs**log.com
  Type:   unauthorized
  Detail: 2400:8902::f03c:93ff:febc:9c54: Invalid response from https://qs****.com/.well-known/acme-challenge/XY4XjjZb_Up_8Je3ju3Sm_qNx0Vs-oyuWOeTrqhhxuE: 404

Hint: The Certificate Authority failed to download the temporary challenge files created by Certbot. Ensure that the listed domains serve their content from the provided --webroot-path/-w and that files created there can be downloaded from the internet.

Cleaning up challenges
Failed to renew certificate qs****.com with error: Some challenges have failed.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
All renewals failed. The following certificates could not be renewed:
  /etc/letsencrypt/live/qs****.com/fullchain.pem (failure)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1 renew failure(s), 0 parse failure(s)
Ask for help or search for solutions at https://community.letsencrypt.org. See the logfile /var/log/letsencrypt/letsencrypt.log or re-run Certbot with -v for more details.



성공

$ docker-compose stop
[+] Running 8/8
 ⠿ Container phpmyadmin  Stopped                                           1.5s
 ⠿ Container certbot     Stopped                                           0.0s
 ⠿ Container npm         Stopped                                           0.0s
 ⠿ Container composer    Stopped                                           0.0s
 ⠿ Container nginx       Stopped                                           0.8s
 ⠿ Container artisan     Stopped                                           0.0s
 ⠿ Container php         Stopped                                           0.6s
 ⠿ Container mysql       Stopped                                           1.4s


$ vi .env
$ docker-compose up -d
[+] Running 8/8
 ⠿ Container phpmyadmin  Started                                           5.8s
 ⠿ Container certbot     Started                                           5.8s
 ⠿ Container php         Started                                           3.8s
 ⠿ Container composer    Started                                           6.0s
 ⠿ Container npm         Started                                           5.1s
 ⠿ Container mysql       Started                                           5.9s
 ⠿ Container nginx       Started                                           9.3s
 ⠿ Container artisan     Started                                           8.9s

$ docker-compose run --rm certbot renew -v
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/qs****.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Certificate is due for renewal, auto-renewing...
Plugins selected: Authenticator webroot, Installer None
Renewing an existing certificate for qs***g.com
Performing the following challenges:
http-01 challenge for qs****.com
Using the webroot path /var/www/certbot for all unmatched domains.
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations, all renewals succeeded: 
  /etc/letsencrypt/live/qs****g.com/fullchain.pem (success)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -