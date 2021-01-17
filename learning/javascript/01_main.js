// 선언을 하는 이유는 자바 스크립트는 처음에 최단기간에 만들어졌고
// flexible 한 언어이므로 선언을 안 하고 사용가능하지만
// ECMAScript 5 에 새로 포함된 use strict는 
// 비상식적인 것을 사용할 수 없게 해서 선언해서
// 에러율을 줄일 수 있다. flexible은 편할 수 있지만 = dangerous 하기도 하다.

'use strict';
console.log('Hello world');

let a; //변수 선언
a = 6;

