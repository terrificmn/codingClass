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
function delay(ms) {
    // setTimeout()에서 지정한 시간뒤에 실행하게 해주는 promise를 만들어서 리턴되게 된다
    return new Promise( (resolve, reject) => {
        setTimeout( resolve, ms) 
    });
}

async function getApple() {
    await delay(2000);  // await은 async 가 붙은 함수에서만 사용할 수가 있다 
    // await이 붙으면 동기적으로 기다려주게 된다
    return 'apple';
}

async function getBanana() {
    await delay(1000);
    return "banana";
}

// 이런식으로 promise를 사용하면 then을 활용해서 시간이 지나고 나서 바나나를 리턴하게 해줄 수가 있다
// async 코드를 풀어서 사용하면 이런 형태가 된다
// function getBanana() {
//     return delay(3000)
//     .then( () => 'banana');   // 이렇게 계속 다른 함수 등으로 (ex. then()) 처럼 이어지는 것을 chaining 이라고 한다
// }


// 이런 식으로 해도 계속 체인닝이 되면서 계속 복잡해지게 된다. 마치 callback 지옥처럼 된다 
function pickFruits() {
    return getApple()
        .then(apple => {
            return getBanana().then(banana => `${apple} + ${banana}`);
        });
}

pickFruits().then(result => console.log(result));  // 이는 생략하면 바로 (then(console.log)) 가 된다

/// 바로 위의 코드를 async 와 awit를 사용하면 더 편하고 쉬운 코드가 된다
async function pickFruitsAsync() {
    const apple = await getApple(); // 호출하고 기다린다.. 이후 블락 block
    const banana = await getBanana(); // 호출하고 기다려 준다 이후 블락된다
    
    return `${apple} + ${banana}`;
}

// async로 만들어진 function이므로 then()을 사용할 수 있다
pickFruitsAsync().then(console.log);

//  async를 사용하면 동기적으로 사용하는 방식으로 할 수 있어서 좋다


/// await의 병렬 처리// 병렬로 실행이 된다
async function pickFruitsAsyncPromise() {
    // async로 await은 코드는 단순해지지만, 결국은 기다리는 것 때문에 문제가 발생할 수가 있다. 그래서 promise를 만들어준다
    const applePromise = getApple();
    const bananaPromise = getBanana(); // 위의 두개의 함수는 async로 되어 있어서 변수에 할당해주면 promise가 만들어진다
    // promise가 만들어지는 순간 벌써 함수로 이동하게 되고 

    // 이후 promise를 await에 넘겨 주게 되면 
    const apple = await applePromise; // 호출하고 여기에 promise 된 변수를 넣어주면 
    const banana = await bananaPromise; 
    
    return `${apple} + ${banana}`;
}

// async로 만들어진 function이므로 then()을 사용할 수 있다
pickFruitsAsyncPromise().then(console.log);


/// useful Promise APIs
// Promise의 all method에 리스트 형식으로 넘겨주면 한꺼번에 수행할 수가 있다. 
function pickAllFruits() {
    return Promise.all( [getApple(), getBanana()])  // 배열로 넘겨주면 다 실행
        .then(fruits => fruits.join(" + "));  // 문자열로 만들어 주기
}
pickAllFruits().then(console.log);

function pickOnlyOne() {
    return Promise.race( [getApple(), getBanana()] ); // 배열로 넘겨주면, 그 중에 빨리 리턴하는 값을 전달(반환한다)
}

// 가장 빨리 수행된 (리턴된 값을)을 사용
pickOnlyOne().then(console.log);