'use strict'

// http: Hypertext Transfer Protocal
// client와 server 간에 hypertext를 주고 받을 수 있도록 만든 규약
// hypertext: 링크, 이미지, html문서 를 의미

// AJAX (에이작스)
// Asynchronous JavaScript And XML
// 웹페이지에서 동적으로 서버에 데이터를 요청을 할 수가 있다 

// XHR (XMLHttpRequest) , 최근에는 fetch() API 등을 사용할 수가 있다. (explorer에서는 안됨에 주의)
// AJAX와 XHR 모두 xml을 이용함

// 역시 최근에는 JSON을 xml 대신에 사용
// JSON : JavaScript Object Notation
// 1999년도 ECMAScript 3rd 에서 나온 Ojbect에 영향을 받아,
// object와 같이 { key: value } 로 만들어지게 되었다

/// simplest datainterchange format
/// lightweight text-based structure
/// easy to read
/// key-value pairs
// used for serialization (직렬) and transmission of data between the network the network connection
// independent programming language and platform



/// 먼저 Object를 serialize를  해주고, 그리고 이 데이터를 서버로 보내고
/// 다시 받은 json을 deserialize를 해서 object로 만드는 과정을 거친다

/// Object to JSON
/// stringfy(object) --- 스트링으로 만들어준다
let json = JSON.stringify(true);
console.log(json);

/// 참고: stringify()함수는 JSON interface에 보면 2개가 정의되어 있는데 이를 overloading 이라고 하며
/// 함수의 이름은 같으나, 파라미터에 따라서 그 각각 다른 함수가 실행되게 된다

json = JSON.stringify( ["apple", "banana"])
console.log(json);


const rabbit = {
    name_: "tokki",
    color: "white",
    size: null,
    birth_date: new Date(),
    jump: () => {
        console.log(`rabbit can jump`);
    },
    // symbol: Symbol("id") -- 변환 안됨
}

/// 여기에서는 함수는 포함이되지 않는다. javascript에서만 사용하는 Symbol도 변환되지 않는다
json = JSON.stringify(rabbit);
console.log(json);

//// stringify()의 생략가능한 두 번째 파라미터는 replacer 인데, 
//// array, 또는 callback function으로 인자로 넘길 수 있다
//// array 형태로 만들어서 해당 key들만 넘겨주게 되면, 그 값들만 json으로 변환된다
json = JSON.stringify(rabbit, ["name_", "color"] );
console.log(json);

//// callback function으로 구성하면 좀 더 세밀하게 가능
//// replacer 파라미터는 key, value 를 전달 받음 (콜백함수)
json = JSON.stringify(rabbit, (key, value) => {
    console.log(`key: ${key}, value: ${value}`);
    // return value;
    return key === "name_" ? "Rabbit" : value;  // 이렇게 조건을 걸어서 리턴해 줄 수도 있다
    // (조건) ? true일때 실행 : else일때 실행
});

console.log(json);


/// JSON to Object
/// parse(json) // 다시 Object로 변환이 됨

// json string을 parse() 함수에 넣어주면 끝
const obj = JSON.parse(json);
console.log(obj);

// 기존 오브젝트인 rabbit에서는 jump()라는 메소드를 사용할 수가 있으나
rabbit.jump();

// string으로 바뀐 JSON에서 스트링으로 변환 된 것이므로, 다시 parsing이 된 Object에서는 jump()같은
// 함수는 사용할 수가 없다. 그냥 스트링일 뿐
// obj.jump(); /// Uncaught TypeError 발생하게 된다. jump는 is not a function

// 또한 Object Date를 통해서 만들어진 birth_date 키, value는 다시 또 getDate()같은 함수를 통해서 
// 또 다른 값들을 받아올 수가 있지만
console.log(rabbit.birth_date.getDate());

/// 이미 스트링으로 변환된 JSON 에서 다시 parsing된 Object obj에서는 그 Date 오브젝트를 사용하는 것이 불가
// console.log(obj.birth_date.getDate()); // 위와 마찬가지로 Uncaught TypeError 발생


/// 스트링으로 바뀐 것을 다시 할 수 있게 하는 방법이 있다 
/// 스트링 이지만, 특정 key를 찾아서 Date()를 만들어서 현재 값을 넣어줄 수가 있다
const obj_1 = JSON.parse(json, (key, value) => {
    console.log(`key: ${key}, value: ${value}`);
    return key === "birth_date" ? new Date(value) : value;
});

console.log(obj_1.birth_date);
console.log(obj_1.birth_date.getDate()); // 이제는 getDate() 메소드를 사용할 수가 있다 





