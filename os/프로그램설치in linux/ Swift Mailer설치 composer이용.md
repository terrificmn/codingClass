# composer를 이용해서 Swift Mailer 다운로드

> 현재는 라라벨을 사용하므로 라라벨에도 mail관련 기능이 있을 듯 한데 추후 찾아보기


**참고내용:  
---swift mailer 기능은   
Swift Mailer can be used with any PHP framework, and   
then easily integrated with an external SMTP like Gmail as well as popular email providers like Mandrill,    
SendGrid, or Mailgun.   

원래 기본sendmail은 외부stpt를 허용 안한다고 하는데 외부smtp를 사용하기 위한   
요런게 가능하다고 함   
    create complex HTML/multipart templates   
    add attachments and embed images  
    send emails via authenticated SMTP, sendmail, Postfix, or your own transport  
    use additional plugins.  

참고 사이트:   
https://blog.mailtrap.io/swiftmailer-sendmail/

**중요!!! 다운로드 그리고 디렉토리 이동해서 할것 그곳에서 설치가 됨   
composer를 인스톨 할 때 --filename으로 이름변경 안했다면 디폴드는 composer.phar 임에 주의   
변경했다면 composer로만 쳐도 되고 아니면 composer.phar로 다 쳐줘야함    

설치 (composer.json에 추가)
```
  $sudo composer.phar require "swiftmailer/swiftmailer:^6.0"
```
또는 
```
  $ composer require "swiftmailer/swiftmailer:^6.0")
```
이렇게 하면 설치가 된다

## 지우는 방법 
composer.json 파일을 열어 보면
```
"require": {
    "php": ">=5.4.0",
    "yiisoft/yii2": "~2.0.6",
    "yiisoft/yii2-bootstrap": "~2.0.0",
    "yiisoft/yii2-swiftmailer": "~2.0.0",
    "dmstr/yii2-adminlte-asset": "2.*",
    "yiisoft/yii2-jui": "*",
    "wbraganca/yii2-dynamicform": "*",
    "kartik-v/yii2-mpdf": "dev-master",   
    "miloschuman/yii2-highcharts-widget": "dev-master",
    "guzzlehttp/guzzle": ">=4.1.4 <7.0",
    "yiisoft/yii2-imagine": "^2.1",
    "kartik-v/yii2-date-range": "dev-master"  <<<-----만약에 이놈을 지운다고 하면 한줄 지우고 저장하기
},
```
여기에서 맨 아래줄에 있는 yii2-date-range 패키지를 지울려고 하면 그 줄 자체를 지워준다

지운다음에 저장을 하고 업데이트 하면 알아서 라이브러리를 지운다고 함  

```
$sudo composer.phar update 
```



