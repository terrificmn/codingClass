'use strict'

// 토끼와 당근 예
// 토끼와 당근이 많이 있다고 할 경우, 예를 들어서 5개씩 있다고 하면  
// 이것들을 한 바구니에 담아두는 것이 자료구조라고 할 수 있다 

// 오브젝트와 다른점은 오브젝트는 토끼의 클래스화이다  
// 토끼의 (fields) properties에는 귀2개, 하얀색털 등이 있고, 뛴다, 먹는다 등의 methods가 있게 되고  
// 당근은 (fields) properties 정도만 있을 수 있는데, 주황색, 비타민c

// 어쨋든 자료구조에서는 한 바구니에 같은 자료형만 담을 수 있다. 즉, 토끼 바구니는 토끼만, 당근 바구니에는 당근만 담을 수가 있는데
// Javascript에서는 서로 다른 자료형도 담을 수가 있다. 
// !! 중요 하지만 다른 자료형을 담는것은 추천하지 않는다

// 배열은 이것을 여러개를 인덱스화에서 만들어주는 것

///// 1. Delaration
// new Array()를 사용하기
const arr1 = new Array();
// 좀 더 많이 사용하는 방법은 bracket을 사용
const arr2 = [1, 2, 3];

/// index position
// 🍎🍋🍌🍒🍓🍑🍉🍋

const fruits = ['🍎', '🍌']
console.log(fruits);
console.log(fruits.length);
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]); // 없는 인덱스를 접근하면 undefined

console.log(fruits[fruits.length -1]); // 마지막 인덱스 접근하기 (총길이의 -1, 0부터시작하므로)


/// looping over an array 
// 전통적인 방법으로 for loop를 사용해서 i (iterator)로 배열의 i 번째를 출력하기
for (let i=0; i < fruits.length; i++) {
    console.log(fruits[i]); 
}

// 좀더 쉽게 -- for of 를 사용
for(let value of fruits) {
    console.log(value);
}

/// forEach 
//forEach는 callback fuction으로 3개의 인자를 전달하는데 컨트롤+클릭을 해서 자세한 api 를 참고
// forEach(callbackfn: (value: T, index: number, array: T[]) => void, thisArg?: any): void;
// 요렇게 나오는데 파라미터로 calbackfn 이 정의되어있고, 그 콜백펑션의 파라미터는 value, index, array로 되어 있는 것을 알 수 있고
// 마지막의 ?는 thisArg가 없어도/있어도 된다는 의미

console.clear();
fruits.forEach(function(fruit, index, array) {
    console.log(fruits, index, array);
});

// javascirpt에서는 이렇게 이름없는 함수를 사용할 수 있는데,  anonymous function 이라고 부른다
// 또한 더 생략을 해서 anonymous function은 화살표 '=>' (이것도함수라고 하는 듯) 기호로 바로 사용할 수도 있는데 
// 이렇게 되면 function 키워드를 사용을 안 하고 ()로 바로 넘겨준다

// 주로 array는 안받아오기도 함
fruits.forEach( (fruit, index) => {
    console.log(fruit, index);
});

// 이런식으로 anonymous 함수는 => 이후에 나오는 것들에서 {} 컬리 브래켓을 생략해도 된다.
/// 오히려 빼는게 많아서 어렵군 ㅋㅋㅋ 하지만 편할 수도..
fruits.forEach( (fruit, index) => console.log(fruit, index) );


// 🍎🍋🍌🍒🍓🍑🍉🍋

////// addition, deletion, copy
// add and item to the end
// push()
fruits.push('🍓', '🍑');
console.log(fruits);

// remove an item from the end
// pop()
fruits.pop();
console.log(fruits);
fruits.pop();
console.log(fruits);

// add an item to the beginning
// unshift
fruits.unshift('🍋', '🍉' );
console.log(fruits);

// remove an item from the beginning
fruits.shift();
console.log(fruits);
fruits.shift();
console.log(fruits);

// 여기에서 push와 pop보다 shift, unshift() 함수가 훨씬 느리다 
// 이유는 다른 데이터는 나두고 마지막 인덱스에서만 사용하기 때문에 빠르다
// 하지만 shift, unshift는 다른 데이터들을 다른 배열로 이동시켜(shift)시켜야 하기 때문에 
// 반복적으로 배열의 길이 만큼 반복을 해줘야 한다. 그래서 느릴 수밖에 없다 


// remove an item by index position
// splice()
fruits.push('🍉', '🍑', '🍋', '🍑', '🍎');
console.log(fruits);

/// 파라미터 중에 ?는 생략이 가능하다는 것 (마우스 오버로 함수 파라미터 확인 시)
// splice 의 함수는 start : number, deleteCount? : number
// type스크립트로 되어 있는데 일단 type은 : 이후로 해줄 수 있는 것 같다. 
// c++의 int start, int deleteCount 의 느낌을 start : number, deleteCount : number 요렇게 표현하는 것 같다
fruits.splice(1, 1);
console.log(fruits);

// 대신 처음 start파라미터에 1번 인덱스만 넣어주고 , delete파라미터 카운트를 생략하면 다 지우게 된다
fruits.splice(1);
console.log(fruits);

// 다시 추가
fruits.push('🍉', '🍑', '🍋', '🍑', '🍎');
console.log(fruits);

// splice 함수에는 optional로 다른 파라미터를 더 넘길 수가 있느데, deleteCount 뒤로 추가로 가능
// 이렇게 되면 지워진 인덱스 이후로 (즉, 그 인덱스에) 추가가 된다 
fruits.splice(1,1, '🍋', '🍎');
console.log(fruits);  // 지워진 1번 인덱스가 지워지고 거기에 레몬, 사과가 들어간 것이 출력
// splice는 join, connect (ropes) by interweaving the strands (weave 해서 이어주는 뜻)


// combinea two arrays; 차례
25:01


