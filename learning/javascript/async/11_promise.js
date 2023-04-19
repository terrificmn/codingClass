'use strict'

// promise 는 자바스크립트에서 비동기를 간편하게 처리할 수 있게 도와주는 오브젝트
// asynchronous operation

// state : 처음에는 pending 상태 
        // 성공적으로 마쳤을 경우에는 fulfilled
        // 실패했을 때는 rejected

// Producer - Consumer 관계

/// Producer
// When new Promise is created, the executor runs automatically
const promise = new Promise( (resolve, reject) => {
    // doing some heavy work (시간이 걸리는 일들에는 async로 처리하는 게 좋다)
    // 예: network, read files 등..
    console.log("doing something");
    // 무엇가 시간이 걸리는 것을 한다고 가정을 하고 2초 뒤에 콜백함수가 실행되어 resolve()가 실행이 되게 한다
    // resolve, reject가 실행되어 리턴되어진 값들이 Promise 객체를 만드는 파라미터로 들어가게 된다 
    setTimeout( () => {
        // 성공적으로 진행했다고 치면 아래 코드 주석해제
        return resolve("gunther");

        // reject를 진행한다고 하면
        // return reject(new Error('no network'));
    }, 2000);
});

// Consumers  - then, catch, finally를 이용해서 사용
// 위의 promise에서 처리된 결과값 resovle()함수로 넘어온 값 
// promise에서는 성공된 값이 넘어오는 리턴되는 것인데 
// 그 리턴된 결과를 다시 이용해서 catch() 를 사용할 수가 있다
promise.
    // then 에는 성공한 값을 처리하게 해주고
    then( (value) => {
        console.log(value);
    })
    // catch에는 실패했을 경우를 처리한다
    .catch( (error) => {
        console.log(error);
    })
    // 비교적 최근에 추가된 기능 finally() 무조건 마지막에 실행하게 되어 있다 
    .finally( () => {
        console.log("finally");
    });



/// Promise chaining
const fetchNumber = new Promise( (resolve, reject) => {
    return setTimeout( () => resolve(1), 1000); // {} 생략 가능
});

/// 계속 결과값을 받은 것을 then() 을 이용해서 처리할 수가 있다
// asynchronous로 받은 값을 계속 처리하게 된다. 즉 처음에 받은 1로 시작
// 콜백 함수에는 return 생략되어 있는 것에 주의, callback이니 나중에 불러주는 함수라고 생각해야겠다
// 즉, 콜백함수의 => 이후의 블럭을 실행을 하고 그 값이 리턴되어져서 그 때 콜백함수가 실행이 되게된다.
// 여기에서 헤깔리는 것은 처음 콜백함수의 파라미터 자체가 또 함수인 듯하다??
fetchNumber.then(num => num * 2)
            .then(num => num * 3)
            // 또는 Promise를 만들어서 또 비동기적으로 처리할 수가 있다
            .then(num => {
                return new Promise( (resolve, reject) => {
                    setTimeout( () => {
                        return resolve(num -1);
                    }, 1000)
                });
            })
            .then(num => console.log(num));


/// Error Handling
const getHen = () => {
    return new Promise( (resolve, reject) => {
        setTimeout( () => {
            return resolve('닭');
        }, 1000);
    });
}

// 뭔놈의 생략이 이렇게 많은지..; 불평을 하지말자 ㅋㅋ
// => 콜백 이후 {} 컬리 브래켓을 생략을 할 수가 있다 // {} 생략이 되면 return도 당근 생략
const getEgg = hen =>
    new Promise( (resolve, reject) => {
        return setTimeout( () => {
            return resolve(`${hen} ==> egg`)
        }, 1000);
    })

const cook = egg => 
    new Promise( (resolve, reject) => {
        // setTimeout( () => resolve(`${egg} ==> 'fried egg`), 1000); // 정상 케이스 resolve() 
        setTimeout( () => reject(new Error(`${egg} ==> 'fried egg`)), 1000);
    });

getHen()
.then(hen => getEgg(hen))
.then(egg => cook(egg))
.then(meal => console.log(meal))  // 여기서의 meal은 마지막 cook으로 부터 넘어온 값이 들어감
// 정상적으로 catch를 하면 reject로 넘어온 경우에는 catch에서 처리할 수 있게 된다 
.catch(error => console.log(error));


// 위에서 getEgg, cook등을 호출할 때 (파라미터부분은) 생략해도 된다
// 받아온 value를 다른 함수로 다시 호출해서 그 함수의 인자로 넘기는 경우에는 (같은 경우) 생략 가능
getHen()
.then(getEgg)
.then(cook)
.then(console.log) // 심지어 콘솔 로그에도 받아온 값이 또 들어가므로 생략가능
// 위에서 reject()를 해서 오류를 발생시킬 경우 catch가 없으면 Uncaught Error가 발생한다 
// 즉, 여기에서는 error 핸들링이 없네 라는 뜻이 된다



21:30 오류처리
