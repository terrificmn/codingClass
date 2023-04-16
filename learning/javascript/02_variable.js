// 선언을 하는 이유는 자바 스크립트는 처음에 최단기간에 만들어졌고
// flexible 한 언어이므로 선언을 안 하고 사용가능하지만
// ECMAScript 5 에 새로 포함된 use strict는 
// 비상식적인 것을 사용할 수 없게 해서 선언해서
// 에러율을 줄일 수 있다. flexible은 편할 수 있지만 = dangerous 하기도 하다.

'use strict';
console.log('Hello world');

let a; //변수 선언
a = 6;

// 2. variable ==== rw (read, write)
// let (added in ES6) 변수 선언


let globalName = 'global various';

{
let name = 'mike';
console.log(name);
name = 'hello';
console.log(name);
console.log(globalName);

}

//var는 ES6 전에 쓰던 방식 -- do not use it
//var hoisting (move, declaration from bottom to top)
// block scope 를 사용할 수 없다. 가장 위로 올라가서 어디에서나 쓰게됨
// 선언이 안되고 쓰면 추후에 꼬일 수 있다.
console.log(age);  //선언이 안되어 있는데 사용이 됨
age = 10;
console.log(age);
var age;

//name = 'mike';
//let name;


//3. constant ===== r(read only)
//// !!NOTE!!
//Immutable data type(변하지 않는): premitive types, frozen objects
//Mutable date types(변하는): all objects(배열) by default are mutable in Java Script

// favor immutable data type always for a few reasons; (값이 변하지 않는것)
// - security 
// - thread safety
// - reduce human mistakes

const daysInWeek = 7;
const maxNumber = 5;


// string
const char = 'c';
const brendan = 'brendan';
const greeting = 'hello' + brendan;
console.log(`value: ${greeting}, type: ${typeof greeting}`);
const helloBob = `Hi ${brendan}!`; // template literals (string)
// ` `로 묶고 쓰면 편하게 하나로 합칠 수 있다. 
// 원래는 ' ' 로 묶으면 중간 중간 ' ' + ' ' +  ' ' 이런식으로 써야한다.
console.log(`value: ${helloBob}, type: ${typeof helloBob}`);


/// boolean
// false: 0, null, undefined, NaN, ''
// true: any other value

const canRead = true;
const test = 3 < 1; /// 이런것도 3이 1보다 작지 않으므로 false로 자동 지정된다

console.log(canRead);
console.log(test);


//null
let nothing = null;
console.log(nothing);


// undefined
let x;
// 또는 let x = undefined; 로 직접 지정해도 된다.
console.log(x);

// symbol, create unique idenfifiers for objects
// 식별자  // 같은 스트링 값을 줘도 식별자로 선언하면 다르게 인식한다.

const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1 === symbol2);  // 문자열 들어간 것은 같지만 식별자로 되어 있어서 다르게 인식함

// Dynamic typing: dynamically typed lanauage 
// 변수에 들어가는 값에 따라서 즉각 타입이 바뀐다.
// 주의해함. 이것도 나중에 프로그래밍 하다가 꼬일 수 있음.

let text = 'hello';
console.log(`value: ${text}, type: ${typeof text}`); //여기에서는 string
text = 1;
console.log(`value: ${text}, type: ${typeof text}`); //여기에서는 number로 바뀜
text = '7' + 5; 
console.log(`value: ${text}, type: ${typeof text}`); ///// 앞에는 문자, 뒤에는 숫자 그러면 문자로 인식해서 붙여준다
text = '8' / '2';console.log(`value: ${text}, type: ${typeof text}`); //여기에서는 문자열을 숫자로 인식해서 나눠준다

//즉각 변수에 들어가는 type에 따라서 계속 자동으로 할당되므로 
// 주의해야함


// object //일상에서 볼 수 있는 물체 박스형태로 생각하면 쉽다.
// real-life object, data structure
const ellie = {name: 'ellie', age: 20};



