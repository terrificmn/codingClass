23분 부터 다시
main도 만들어야 할듯


/// callback 지옥 리팩토링 -- 10_callback.js 의 내용을 수정
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
        // 그리고 setTimeout에 설정한 2초로 지연이 됨
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
