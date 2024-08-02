
// true 는 0이 아닌 경우 0보다 큰 1 부터 모든 숫자가 있을 경우 (-1  이하도 마찬가지이다.),  [] 빈 배열 true 이유는 object이기 때문이다.
// false 0, -0, '',"" 빈 문자열, null, undefined,

if(-1) {
    console.log("Yes, it is true");
}

if(undefined) {
    console.log("It is true");
} else {
    console.log("It is false");
}

if([]) {
    console.log("array is true");
} else {
    console.log("It is false");
}



let num;
/// 이유는 num은 선언은 되었지만 할당이 안되었으므로 js에서는 이를 undefined 라고 한다. 그러므로 false
if(num) {
    console.log("num is true");
} else {
    console.log("num is false");
}

// js 에서는 && 연산자를 이용해서 true 일 경우에 진행할 수 있게 하는 코드로 활용

let obj;
obj && console.log(obj.name);

// 이렇게 하면 obj 가 undefined이기 때문에 name 이라는 변수를 접근하면 에러가 발생하지만, && 연산을 이용해서 실행이 안되게 하는 방식

let obj2 = {
    name : "obj2-hello"
}
obj2 && console.log(obj2.name);

