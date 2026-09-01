## yarn 설치하기 (global)
```
npm install --location=global yarn
```

또는 `npm install -g yarn`
> 단, -g, --global 은 deprecated 되었다고 하나, 사용은 가능하다

## yarn 빌드 실패
`yarn build` 할 경우에 특정 패키지에서 에러가 발생하는 경우  

ERR_OSSL_EVP_UNSUPPORTED   
대충 아래 처럼 발생한다.  
```
 { opensslErrorStack: ['error:03000086:digital envelope routines::initialization error'], library: 'digital envelope routines', reason: 'unsupported', code: 'ERR_OSSL_EVP_UNSUPPORTED' }
```

터미널에 변수를 등록해준다. 
```
export NODE_OPTIONS=--openssl-legacy-provider
```

이유는 OpenSSL 3.0 에서는 알고리즘, 키 사이즈를 변경하려고 하면  
허용이 안되게 업데이트 되었다고 한다. 
Node.js to the latest LTS version 을 사용 (18번 이상) 하거나,  
위의 옵션을 export 해주면 사용할 수가 있다.


