/// number, string, boolean, null, undefined
// 등 가장 기초적인 변수들을 primitive type이라고 할 수 있다.

let a = 10;
console.log(a);

const num = 2;

// num = 10; // 이런식으로 const 상수 변수는 당연히 변경이 불가능  
// Uncaught TypeError: invalid assignment to const 'num'

// 기본적으로 새로운 변수를 만들어서 할당을 하면 copy가 된다.
let num2 = num;
console.log(num2);


/// object
// 키, value로 구성된 primitive 변수들 외에 것들은 js에서는 모두 object라고 생각하면 되고   
// 배열 등도 object에 포함된다.
// 여러 변수들이 구성되어 있을 수가 있다.

let obj = {
    name : "Gunther",
    age : 40
}

let obj2 = obj;
console.log(obj2.name);

// 보통의 primitive 변수들이 카피되는 방식과는 다르게 object는 주소 혹은 레퍼런스 값만 가지고 만들어진다.   
// 그렇기 때문에 실제 안에 있는 '키'들은 primitive 방식의 변수들로 구성이 되어 있고   
// 이것을 reference로 삼기 때문에 카피된 obj2의 키 벨류를 변경하면 obj1도 변경이 된다.  
// 즉, 해당 object의 변수들까지 복사되는 것은 아니다.

obj2.name = "Hello";
console.log(obj2.name);
console.log(obj.name);

// 여기에서 보면 obj 까지 바뀐 것을 알 수 있다



