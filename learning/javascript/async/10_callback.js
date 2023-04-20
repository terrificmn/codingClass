'use strict';

// JavaScript is synchronous.
// Execute the code block in order after hoisting
// 순차적으로 동기화 되서 사용되는 것
// hoisting 이란  var, function declaration 등의 선언등이 가장 위로 올라가는 것을 의미
// hosit 의 사전적 의미는 rope나 pulley(기어)등을 이용해서 끌어올리는 것을 의미 

console.log('1');
console.log('2');
console.log('3');
// 이렇게 실행을 해보면 순서대로 당연히 실행이 된다 

console.log('1');
// setTimeout() 함수는 콜백함수와, ms 를 받는다
// 이렇게 되면 비동기적으로 실행이 된다 
// 즉, 나중에 '다시 불러줘' 라는 의미가 되므로 callback function 이 되는 것
// 그래서  setTimeout은 1000 ms, 1 초 뒤에 function()을 call 해서 실행을 하게 된다 
setTimeout( function() {
    console.log('2');
}, 1000)
console.log('3');


// Synchronous callback
function printImmediately(print) {
    print();
}

printImmediately( () => console.log("hello"));


/// Asynchronous callback
function printWithDealy(print, timeout) {
    setTimeout(print, timeout);
}

printWithDealy( () => console.log("async callback"), 2000);

// 위의 결과를 보면 모든 함수들이 hoisting이 되어 가장 위로 올라가서 선언되어지고   
// 그리고 동기적으로 synchronous로 실행 되다가 
// 콜백함수 등을 만나면 브라우저에 요청한 시간 만큼 지연된 후 브라우저에서 해당 콜백함수를 실행해서 비동기로 실행이 되게 된다 



//// 콜백 지옥!!
/// callback hell 
class UserStorage {
    loginUser(id, password, onSuccess, onError) {
        // 2초 뒤에 실행이 되는 것으로 설정
        setTimeout( () => {
            if((id === "mike" && password === "hello" ) || (id === "coder" && password === "world")) {
                onSuccess(id);
            } else {
                onError(new Error("not found"));
            }
        }, 2000);
    }

    getRoles(user, onSuccess, onError) {
        // 2초 뒤에 실행이 되는 것으로 설정
        setTimeout( () => {
            if(id === "mike") {
                onSuccess( { name: "mike", role: "admin" });
            } else {
                onError(new Error("no Access"));
            }
        }, 1000);
    }
}


const userStorage = new UserStorage();
// prompt() 함수는 입력을 받는 창을 띄워준다
const id = prompt("enter your id");
const pwd =  prompt("enter your password");

userStorage.loginUser(
    id, pwd,
    // 동기적으로 user 넘겨주는 파라미터의 콜백함수는 나중에 실행이 되고, loginUser()의 함수가 먼저 실행되게 된다 
    user => {
        // getRoles() 함수에서는 onSuccess가 필요한데, 이미 longinUser()에서 id를 체크해서 onSuccess가 설정이 된다 
        // loginUser() 메소드에는 4개의 아규먼트가 필요한데, 로그인이 성공적으로 되었는지를 확인하는  
        // onSuccess, onError 파라미터에 대응하기 위한 콜백함수를 사용했다  
        // onSuccess부분: 콜백함수가 사용되었는데 getRoles() 메소드를 호출해서 그 결과를 리턴하는데 또 그안에 콜백함수들이 계속 있는 경우임 
        // 그리고 각각의 메소드는 setTimeout에 설정한 2초로 지연이 되어 수행
        userStorage.getRoles(
            user,
            userWithRole => {
                alert(`hello ${userWithRole.name}, you're now an ${userWithRole.role}`);
            },
            error => {
                console.log(error);
            }
        );
    },
    error => {
        console.log(error);
    }
);

// 위 처럼 계속 콜백을 사용하게 되면, 한눈에 알아보기 어렵고 복잡해진다.
// 디버깅 해야하는 경우에도 어렵다. 콜백 체인이 길어지면 길어 질 수록 유지보수 등 어렵게 된다 
// 콜백안에서 호출하고 또 콟백에서 또 호출하고 복잡해진다

