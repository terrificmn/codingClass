'use strict'
// 기존에 있던 api에서 좀 더 나은 방식으로 방법을 제공하거나  
// 기존에 있던 코드를 감싸서 api를 제공하는 것을 'syntactic sugar'라고 한다 
// async와 await도 기존에 있던 Promise를 좀 더 편하게 할 수 있게 제공한다고 함
// JavaScript에서는 클래스가 그 예로 들 수 있다. prototype위에 (원래 js 있던 녀석)에 붙여진 것이라고 할 수 있다고 한다

// async & await
// clear style of using promis  // 상황에 따라 promise를 사용하는게 더 맞을 경우도 있다

/// promise
function fetchUser() {
    // do network request in 10 secs /// 10초 걸리는 상황
    // 일단 Promise를 사용해서 then()를 사용해서 콜백함수를 사용하면 시간이 지난 다음에 처리해주는게 된다 (비동기 aync로 처리해주게 된다)
    // Promise에는 resolve, reject라는 executor를 등록하게 되는데 각각의 콜백 함수를 받게 되어 있다
    // Promise {}안에는 asynchronous로 수행이 되게 된다
    return new Promise( (resolve, reject) => {

        // return 'Hello';  // roslve, reject를 완료를 시켜줘야한다. resolve() 넣지 않는다면 state는 pending 상태가 된다
        return resolve('Hello'); // 그러면 state가 fulfilled로 바뀌고 value가 등록이 된다
    });
}

// javascript는 동기적으로 한줄 한줄 실행하기 때문에 
// 해당 fetchUser()에 가서 10초 동안 머무르게 되었다. 그러면 block이 되게 되고 
// 그 다음 수행할 것은 10초가 지나야지 동기적으로 수행이 된다 
const user = fetchUser();
console.log(user);


/// async
/// 기존의 promise를 사용하던 방식에서 함수 앞에 async라고 해주면 그 안의 내용을 promise로 만들어준다
/// promise를 생성할 필요가 없이 사용하게 된다
async function fetchUserAsync() {
    return "hello";
}

// async를 넣은 function은 자동으로 promise가 생성이 되어서 객체 생성 후에도 
// then을 이용해서 사용할 수 가 있다
const user_async = fetchUserAsync();
user_async.then(console.log);
console.log(user_async);


/// await 
await 7:40