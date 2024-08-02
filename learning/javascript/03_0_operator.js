// 1. String concatenation
console.log('my' + ' cat');
console.log('1' + 2);  // 뒤에 숫자를 문자열로 자동 변환해서 표시
console.log(`string literals: 1 + 2 = ${1 + 2}`);
// ``표시로 사용할 때는 중간에 $변수로 계산을 해서 넣을 수도 있다.
// 참고: single quote 를 사용할 때는 줄바꿈은 \n, 탭은 \t 이다

// 2. Numeric operators
console.log(1 + 1); //add 
console.log(1 - 1);  //substract
console.log(1 / 1);  //divide
console.log(1 * 1);  // multiply
console.log(5 % 2);  // remainder 나눈 나머지 값
console.log(2 ** 3);  // exponentiation  제곱 (2에 3승)

// 3. Increment and Decrement operators
let counter = 2;
const preIncrement = ++counter; // preincrement 가 된다 변수에 업데이트가 먼저 된 후 (+1) counter변수 값을 더함 
// counter = counter + 1;
// preIncrement = counter;
console.log(`preIncrement: ${preIncrement}, counter: ${counter}`);


const postIncrement = counter++;
// postIncrement = counter;  //preincrement와 다른점은 postIncrement상수에 counter변수값을 먼저 넣은 뒤에 +1 한다
// counter = counter + 1;
console.log(`postIncrement: ${postIncrement}, counter: ${counter}`);

/// 마이너스도 같다 Decrement
//
counter = 1;
const preDecrement = --counter;  //업데이트 (-1 후) 변수값을 상수preDecrement에 준다
const postDecrement = counter++; // 변수 counter의 value를 먼저 상수postDecrement에서 할당한 후 업데이트 (-1시킴)

// 4. Assignment operators
let x = 3;
let y = 6;
// 반복되는 등호를 생략해서 많이 사용하게 된다.
x += y; /// x = x + y;랑 같다 (줄임말)
x -= y;
x *= y;
x /= y;


// 5. Comparison operators
console.log(10 < 6); 
console.log(10 <= 6);
console.log(10 > 6);
console.log(10 >= 6);



// 6. Logical operators: ||(or) &&(and)  !(not)
const value1 = false;  //false
const value2 = 4 < 2;  //true

/// || (or), finds the first truthy value (처음으로 true 값이 나오면 멈춘다)
console.log(`or: ${value1 || value2 || check()}`);  
// 즉 value2 에서 true 이므로 value2만 확인하고 끝

// 중요: OR은 조건을 하나만 만족하면 연산을 끝내는거에 주목한다.
// 즉 value1 이 false 이므로 뒤의 value2 와 check()함수는 실행을 안함
// * 중요: 효율적 코드작성:
//예를 들어 쉽게 연산이 끝나지 않을 함수등을 처음에 넣어서 computation
//많이 하게 하는 것은 좋은 코딩 방법이 아니다!! (처음에만 맞으면 true 이면 끝)
// 그래서 헤비한 연산을 할 듯 하면 뒤로 배치해서 하는게 좋다 (코드작성시)


//// && (and) 연산자: 모두가 true 이여야 한다!!
// 그래서  finds the first falsy value 처음 조건이 false면 어차피 파토! ㅋㅋ
console.log(`and: ${value1 && value2 && check()}`)
// 마찬가지로 효율적으로 코딩할려면 헤비한 코드 조건은 뒤로 배치하는게 좋다
// often used to compress long if-staement
// nullableObject && nullableObject.something -----------이러면 and 조건이어서
/// 널 값을 체크할 떄 처음에 false면 다 확인을 안할테니 이런식으로 사용한다고 한다.

function check() {
    for (let i =0; i < 10; i++) {
        // wasting time
        console.log('얍');
    }
    return true;
}


/// !(not) 연산자  : 값을 반대로 바꾼다. 
console.log(!value1); // 예를 value1이 false가 들어가 있는데 반대값 true 바꿈


/// 7. Equality 
const stringFive = '5';
const numberFive = 5;

// == loose equality, with type conversion, 즉 타입은 보지 않는다.
console.log(stringFive == numberFive);  
console.log(stringFive != numberFive);

// === strict equality, no type conversion, 즉 타입까지 같아야 한다.
console.log(stringFive === numberFive);  
console.log(stringFive !== numberFive);

// object equality by reference
const ellie1 = { name: 'ellie'};  // value는 같지만 ellie2 와는 다른 reference를 가리킴
const ellie2 = { name: 'ellie'};  // value는 같지만 ellie1 와는 다른 reference를 가리킴
const ellie3 = ellie1;  // 이것은 레퍼런스가 같은곳을 가리킴

console.log(ellie1 == ellie2);  // value가 같아도 reference가 다르므로 false
console.log(ellie1 === ellie2); // type을(그리고 value도) 보기도 전에 reference가 다르므로 false
console.log(ellie1 === ellie3);  // reference 가 같아서 true




// equlitiy -puzzle  
// 0,null 값은 false 값을 여겨지지만 type까지도 같은것은 아님에 주의!
console.log(0 == false);   // 0은 false로 간주---> true
console.log(0 === false);  // 0은 false로 간주하지만 boolean 타입은 아니다!--> false
console.log('' == false);  // null은 false로 간주 --->true
console.log('' === false); // null은 boolean 타입은 아님 --> false
console.log(null == undefined);  // 같은 값으로 인정---true
console.log(null === undefined); // 타입은 다르다 --false


// 8. Conditional operators: if
// if, else if, else
console.log('HERE');

const name = 'ellie';
if (name === 'mike') {
    console.log('welcome, mike');
} else if (name === 'coder') {
    console.log('You are an amazing coder');
    } else {
        console.log('unknown');
    }


    // 9. Ternary operator: ? 
// condition ? value1 : value2;  //간단하게 if문을 사용할 때 
// 조건 다음에 ? 을 붙이면 true 이면 그 다음코드 실행 아니면 :(콜론) 코드 뒤를 실행함

console.log(name === 'ellie' ? 'yes' : 'no');

// 간단한 조건에만 사용하는게 좋다!!


// 10. Switch statement
// use for multiple if checks
// use for enum-like value check
// use for multiple type checks in TS (TimeScript)
const browser = 'Firefox';
switch (browser) {
    case 'IE':
        console.log('go away!');
        break;
    case 'Chrome':
        console.log('love you!');
        break;
    case 'Firefox':
        console.log('love you!');
        break;
    ///여기에서 같은 결과가 필요한거라면 case 를 연달아 붙이면 된다
    /// 예:
    //case 'Chrome':
    //case 'Firefox':
    ////console.log('love you!');   // 이런식으로..
    default:     // default 값을 정해준다 
        console.log('same all!');
        break;   // 언제나 브레이크로 빠져나오게 한다.
}


// 11. Loops  (true이면 계속 반복. 즉, false가 나올 때까지 loop)
// while loop, while the condition is truthy,
// body code is executed
let i = 3;
while (i>0) {
    console.log(`while: ${i}`);
    i--;
}


// do while loop, body code is executed first,
// then check the condition

do {   // do while 문은 일단 한번은 실행한 다음에 조건을 체크한다
    console.log(`do while: ${i}`);
    i--;
} while (i > 0); // 이 코드에서는 상수 i는 이미 위의 코드에서 0이 
                // 들어가 있어서 i는 0보다 크지 않지만 (false) 그래서 
                // 실행은 안해야하지만 (while loop라면)
                // 일단 do 안에 있는 코드를 한번 실행하게 된다.


// for loop, for(begin; condition; step)
for (i = 3; i > 0; i--) {   // 처음 변수 i에 값을 준 후 조건에 맞으면 반복
    console.log(`for loop: ${i}`); //블럭안의 코드 실행하고 i-- 시키고 다시 조건문체크
    // 그리고 다시 조건이 true 이면 또 반복
}

// for (let i = 3; i > 0; i = i - 2) {   //i 변수를 for문안에서 선언해도 된다.
    // inline variable declaration  (지역변수로 선언하고 사용해도 됨)
//    console.log(`inline variable for: ${i}`);
// }

// nested loops   // 이중으로 for loop 될 수 있게 하는것
//for (i = 0; i < 10; i++) {   // i가 조건에 맞을 때 1번 실행될 때 j 루프에서는 9번 실행됨
//    for (let j = 0; j < 10; j++) {
//        console.log(`i: ${i}, j: ${j}`);
//    }
//}

// O(n2제곱) 이 실행된다. 즉 i가 한번 돌 떄 j는 10번 (i는 총 10번 수행해야함)
// 그래서 10에 2제곱 그래서 100번이 실행된다.
// CPU에 부담을 많이 주게 되는 코드일 수 있다. 
// 되도록이면 피하는게 좋다. 주의하자!

// 퀴즈 
// break, continue 를 이용
// Q1. iterate from 0 to 10 and print only even numbers using continue
// (짝수에만 실행되게 해보자 - continue 이용

for(i = 0; i < 11; i++) {
    if(i % 2 !== 0) {  // 나눠서 몫이 0과 같지 않다면 (홀수라면) continue 호출해서
        continue;  // 바로 {}안의 for문을 수행: 다음을 코드를 실행하지 않고 바로 i++ 하고 다시한번 loop 실행
    }
    console.log(`even number is ${i}`);  //0이면 코드 실행
}


// Q2. iterate from 0 to 10 and print numbers until reaching 8 using break
// 8이 나오면 멈추게 해보자 break 이용
i = 0;
while (i < 10) {
    i++;
       if (i > 8) {
       break; // for문 {블럭을 벗어난다
       }
     console.log(`${i}`);
}

