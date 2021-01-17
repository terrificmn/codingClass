// Function
// - fundamental building block in the program
// - subprogram can be used multiple times
// - preforms a task or clacultaes a value

// 1. Function declaration
// function name(parameter1, parameter2) { body... return;}
// one function === one thing 함수는 하나의 일만 하는것이 좋다
// naming: verb형태, command 형태로 이름을 만든다. doSomething
// ****참고 variable은 noun 형태로 이름을 만드는게 좋다.****
// e.g. createCardAndPoint -> createCard, createPoint
// 너무 다양한 기능을 하지는 않는지 고민해 보아야한다.
// function si object in JavaScript

function printHello() {
  console.log('hello');
}

printHello();  //함수를 부르면 수행하는것 
// 사실 이런 함수는 별 기능이 없다  - parameter를 넘겨주어야한다 */

function log(message) {
    console.log(message);
}
log('Hello@');
log(12345);
// 이런식으로 function log에 message라는 파라미터 값을 받을 수 있고 
// 함수를 부를 때 값을 넘겨주면 기능을 수행하는데
// JS는 타입을 안 따지므로 string 이나 integer도 알아서 출력해 주는데
// 자동으로 변환되니 쉬운 면도 있으나 좋은 습관은 아니다.
// *** 참고: 타입이 중요한 경우에는 곤란해 질 수도 있다. ***

// *** TypeScript 로 변환 하면.. 참고:; ***
// function log(message: string): number {  타입을 명시해줘야 한다. 리턴값도 지정해줘야한다.
//    console.log(message);
//    return 0;  //리턴값을 0으로 준다. // 위에 파라미터 리턴값을 숫자로 정의했기 때문에
// }
// ***///

// 2. Parameters
// premitive parameters: passed by value
// object parameters: passed by reference
function changeName(obj) {
    obj.name = 'coder';
}
const ellie = { name: 'ellie'};


// 상수 ellie를 정의하고
// object해서 name이라는 것을 만들고 그곳에 ellie라고 넣어준다.
// 이것을 상수 ellie에 메모리에는 reference값을 가지고 있는다.
// 이 reference에는 메모리 어딘가를 가리키고 있다.

// -----상수ellie------->reference----->name.ellie

changeName(ellie);
console.log(ellie);

// 3. Default parameters (added in ES6) ES6에서 추가됨
function showMessage(message, from) {  //파라미터 2개를 받음
    console.log(`${message} by ${from}`);
}
showMessage('HI!');  //파라미터 한가지만 (메세지)만 전달함. from값을 전달 안했기 때문에
// 결과는 HI! by undefined 로 나오게 된댜ㅏ.

//그래서 파라미터 옆에 디폴트 값을 지정해 놓을 수 가 있다.
// function showMessage(message, from = 'unknow'))
// 위 처럼 디폴트 값을 줄 수 있다.


// 4. Rest parameters (added in ES6)
// function이 object 이기도 한 이유는 
// 다양한 속성값을 가지게 된다.
// e.g. arguments, caller, length, name 등...

function printAll (...args) { //... 을 쓰면 배열 형태로 전달됨 (rest parameters) 
    for (let i = 0; i < args.length; i++) {  //args parmeter의 배열만큼
        console.log(args[i]);
    }
}
printAll('dream', 'coding', 'ellie');
// 3개의 인자를 전달하면 함수에서 ... 으로 받으면 배열로 받아진다

/*
for (const arg of args) {
    console.log(arg);
}
///for문의 of 문법을 이용해서 같은 결과값을 낼 수 있다.

args.forEach((arg) => console.log(arg));
// forEach함수를 이용해서 같은 결과값을 낼 수 있는 방법.
*/

// 5. Local scope
// 밖에서는 안이 보이지 않고
// 안에서만 밖을 볼 수 있다.
// 함수안에서 변수를 선언하면 지역변수가 된다.
// 그래서 변수를 함수 밖에서 호출하면 에러가 된다.
// 함수 안에서는 글로번 (전역변수) 이면 사용할 수 있다.
// 이것을 밖을 본다는 의미로 scope 라고 하는 듯

let globalMessage = 'global' // global varible
function printMessage() {
    let message = 'hello';
    console.log(message); // local variable
    console.log(globalMessage);
        function printAnother() { //이렇게 함수안에 또 함수를 생성한다면..
            console.log(message);  //위의 함수 즉 부모 함수에서 선언했던 message를 사용할 수 있다.
            let childMessage = 'hello';  
        }    

       // console.log(childMessage);  // 두번째 함수(즉 자식함수)에서 선언한 childMessage는 
        // 한단계 위인 함수레벨에서 (즉, 부모함수)에서 사용하려고 하면
        // childMessage is not defined 로 에러가 발생하며 사용할 수 없다.
}
    //console.log(message);  //이렇게 밖에서 호출하면 에러가 남
    //(message is not defined 왜냐면 함수안에서 선언했기 때문에 local variable)

printMessage();

//즉, 상속은 부모에서 자식으로 이어지지만 위로는 안 이루어진다

// 6. Return a value
function sum(a, b) {
    return a + b;
}
const result = sum(1, 2); //3을 리턴 받는다
console.log(`sum: ${sum(1, 2)}`);
// 모든 함수는 리턴을 하게 되는데
// 리턴값이 생략되어 있는 경우는 retrun undefined; 가 생략되어 있는 것

// 7. Early return, early exit
// bad logic 예
/*
function ungradeUser(user) {
    if (user.point > 10) {
        // long upgrade logic... //  가독성이 떨어지게 된다..
    }
}
*/
// good logic 예
function ungradeUser(user) {
    if (user.point <= 10) {  // 조건이 맞지 않을 때는 빨리 리턴을 해버리는 로직
      return;
    }
    // long upgrade logic... 조건이 맞을 때에 수행할 로직을 수행하는 것이 더 좋다
}

// 조건이 맞지 않는 경우 
// undefinded, -1 인 경우 
// 빨리 리턴을 한 후 맞는 경우에 필요한 로직을 짜주는 것이 좋다고 함.


// First-class function
// function are treated like any other variable
// can be assigned as a value to variable
// can be passed as an argumnet to other functions.
// can be returned by another function

//  1. Function expression
// a function declaration can be called earlier than it is defiend. (hoisted)
// a fucntion expression is created when the execution reaches it.

const print = function () {  //함수를 선언함과 동시에 변수에 할당; 함수의 이름이 없음
       // anonymous function
    console.log('print');
}
print(); 

const printAgain = print;  // printAgain 에다가 print를 주고
printAgain();  //printAgain을 호출하면 function 함수를 하는것과 같은 효과

// 함수를 부르는 것 (function expression)은 함수가 정의가 되기전에 부르면 에러가 난다
// 하지만 함수를 부르면  어딘가에 함수가 정의(function declaration)이 되어 있으면
// JS에서는 함수들 정의 된것을 먼저 처리해서 
// 함수정의 앞에서 써도 사용이 가능한 차이가 있다.

// 2. Callback function using function expression
function randomQuiz(answer, printYes, printNo) {
    if (answer === 'love you') {
        printYes();  //true면 printYes()함수를 호출
    } else {
        printNo();  //false면 printNo()호출  함수는 아래에 정의되어 있으니 호출가능
    }
}

const printYes = function () {  //함수에 이름이 없는 것을 anonymous function이라고 함
    console.log('yes!');
}

const printNo = function print() { // 함수에 이름이 있으면 named function
    console.log('no!');
    // print(); // recursions 함수에서 함수를 또 부르는 것 
    // 이러면 계속 수행을 계속해서 하므로 프로그램이 다운되거나 할 수 있다.
    // 특수한 경우에 사용한다고 한다. e.g. 뭔가 테스트하거나 ..
}
// named function은
// better debugging in debugger's stack traces

randomQuiz('wrong', printYes, printNo);
randomQuiz('love you', printYes, printNo);


// Arrow Function
// always anonymous
// arrow function은 항상 이름없는 함수로 정의되어야 함
// anonymous 함수로 만들고 {}도 넣어 줘야하는데..

/* 이렇게 만들어야 한다..
const simplePrint = function () {      
    console.log('simplePrint!');
}
*/

/* 위의 함수와 같은 내용을 => 애로우로 표시 그래서 애로우 함수
// 함수이름을 아예 빼버리고 ()만 남김, {}괄호도 필요없음
// 간결하게 표현할 수 있는 장점이 있어서 나중에 배열, 리스트 등을 다룰 때 더 좋다
*/
const simplePrint = () => console.log('simplePrint1');
/*
문제 : add 변수(상수)에 파라미터 a, b를 받아서 a + b값을 리턴하는 함수를 만든다면..
// 이것을 애로우함수로 표현하면 훨씬 간결해진다.
*/
const add = (a, b) => a + b;
/* 원래 정규 함수표현은.. 이런식으로
const add = function (a, b) {
    return a + b;
}
*/
// 블럭을 넣어서 함수안에서 더 많은 내용을 처리해야한다면 {}를 해주고 그 안에서 
// 리턴 키워드로 값을 리턴해줘야만 한다
const simpleMultiply = (a, b) => {
    return a * b;
}

console.log(`${simpleMultiply(2, 2)}`);


// 추가. IIFE: Immediately Invoked Function Expression
// 함수를 선언함과 동시에 바로 호출하기
/*
function Hello() {
    console.log('IIFE');
}
Hello(); //이런식으로 추후에 함수를 호출
*/

//하지만 동시에 호출하려면 함수자체를 ()로 묶고 다시 ()로 호출한다
(function Hello() {
    console.log('IIFE');
})();


6번 객체지향언어 볼 차례
