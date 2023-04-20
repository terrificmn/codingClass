'use strict'

/// callback 지옥 리팩토링 -- 10_callback.js 의 내용을 수정
// UserStorage클래스의 메소드에서 그 전 callback hell 버전은 파라미터로
// onSuccess, onError를 받았는데, 이 2개의 파라미터를 콜백함수를 호출해서 수행을 한 다음에  
// 받는 것으로 했었는데..그 안에 계속 콜백 함수들이 있었다...
// 이제는 그 콜백 함수는 필요가 없고, Promise 클래스를 이용해서 처리해주게 되면 
// 실제 인스턴스를 만들고 수행할 때는 then(), catch()을 사용해서 처리

class UserStorage {
    loginUser(id, password) {
        return new Promise((resolve, reject) => {
            // 2초 뒤에 실행이 되는 것으로 설정
            setTimeout( () => {
                if((id === "mike" && password === "hello" ) || (id === "coder" && password === "world")) {
                    resolve(id);
                } else {
                    reject(new Error("not found"));
                }
            }, 2000);
        });
        
    }

    getRoles(user) {
        return new Promise((resolve, reject) => {
            // 2초 뒤에 실행이 되는 것으로 설정
            setTimeout( () => {
                if(id === "mike") {
                    resolve( { name: "mike", role: "admin" });
                } else {
                    reject(new Error("no Access"));
                }
            }, 1000);
        });
        
    }
}


const userStorage = new UserStorage();
// prompt() 함수는 입력을 받는 창을 띄워준다
const id = prompt("enter your id");
const pwd =  prompt("enter your password");

// user에게 입력을 받은 후에는 then을 이용해서 처리, 에러는 catch를 이용한다
userStorage.loginUser(id, pwd)
    .then(user => userStorage.getRoles(user))  // 콜백함수에 넘겨줄 인자가 같을 경우는 생략가능 // .then(userStorage.getRoles)
    .then(user => {
            return alert(`Hello ${user.name}, You are ${user.role} role`)
    })
    .catch(user => {
        console.log(user);
        return alert('You are not a member');
    });  // 콘솔만 찍을 시 .catch(user => console.log(user))  콜백 함수로 념겨줄 아규먼트와 콜백함수에서 사용할 변수가 같다면 생략 가능 
        // .catch(consol.log)


