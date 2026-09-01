// 변수에는 하나의 값만 들어가는데  

let name = 'gunther';
let age = '30';

print(name, age);

function print(name, age) {
    console.log(name);
    console.log(age);
}

// 이런식으로 사용을 해야하지만 object를 사용하게 되면 좀 더 편하게 관리될 수 있다
// c의 construct 같은 느낌

// object 만들기
const obj1 = {}  // {} 컬리 브래킷으로 만들면 object가 된다 -- 'object literal' syntax라고 한다
const obj2 = new Object(); // 클래스 Object를 이용해서 만들어도 된다  -- 'object constructor' syntax라고 한다 

function print1(person) {
    console.log(person.name);
    console.log(person.age);
}

// 클래스 없이 바로 object를 생성할 수가 있다. 괄호{} 컬리 브래켓에 그냥 만들어 주면됨
const gunther = { name: 'gunther', age: 4 };
print1(gunther);


// javascript에서는 다른 언어와는 조금 다르게 나중에(뒤에서) 새로운 property, 즉 fields (멤버 변수) 등을 추가할 수가 있다
// 하지만 너무 동적인 요소가 되므로 많이 사용하는 것은 금물
gunther.has_jab = true;
console.log(gunther.has_jab);

// 뒤늦게 property를 삭제할 수도 있는 미친(?) 기능도 있다
delete gunther.has_jab;
console.log(gunther.has_jab);    // undefined로 출력되게 된다

/// object는 Key, Value 로 구성된다
// { Key : value }; 로 만들어진다 


////// computed properties
// 보통 property를 가져올 때는 . 키워드를 사용하는데 
console.log(gunther.name);

// 배열을 사용할 수가 있다  -- 대신 인덱스가 아닌 키(key)로 확인을 할 수가 있다 -- associative array 식으로 접근이가능
/// key should be always string
console.log(gunther['name']);

// 다시 할당하기 
gunther['has_job'] = true;
console.log(gunther.has_jab);

// 코딩하는 경우에는 닷 (.)을 사용해서 하면 되고 , 
// 런닝타임에서 결정될 경우에는 어떤 값일지 정확히 모를경우에  
// computed properties 방식으로 사용할 수가 있다고 한다

// 즉, 아래의 경우 처럼 사용하게 된다 
// 만약 key 라는 파라미터를 입력을 받아서 하는 함수가 있다고 가정을 했을 경우
function printValue(obj, key) {
    console.log(obj.key);   // undefinded가 되게 된다. key는 정의 되어 있지 않기 때문 // 이렇게 key자체가 특정 따로 있는 변수가 아닌, 
    // 어떤 object 안의 property를 받을 경우에 사용하는 경우에 사용된다 
    // 어떤 object를 넘기는데 그 안의 key값을 같이 보여줄 수 있는 경우인데, 이럴 경우에는 computed property 형식을 사용해야 undefined가 안됨

    console.log(obj[key]);  // 이렇게 하면 추후 함수에서 호출되었을 때 들어오는 아규먼트를 보고 key값의 value를 보여주게 된다
}


printValue(gunther, 'name'); // string으로 키값을 전달 해야하고, 어떤 property를 정해져 있는 것이 아닌, 다른 키을 넘겨줄 수가 있다
printValue(gunther, 'age'); // key자체가 파라미터 이기 때문에 age 도 넘길 수가 있다


/////Property value shortened
const person1 = { name: "Bob", age: 20};
const person2 = { name: "Steve", age: 25 };
const person3 = { name: "Mike", age: 23};

// 위와 같은 방법으로 하나씩 오브젝트를 만드는상황인데 여기에서 함수를 만들어서 오브젝트 만들어서 리턴한다고 하면 
// 이런식으로 만들어진다 

const person4 = makePerson("Gunther", 30);
function makePerson(name, age) {
    return {
        name: name,
        // age: age,
        // 이럴 경우 key, value의 변수 이름이 동일한 경우 아예 생략하고 하나만 써줘도 된다 
        // 이게 바로 shortened 
        // name,
        age
    };
}

console.log(person4);

/// constructor Function
// 위와 같은 방법을 자바 스크립트에서는 클래스 처럼 사용할 수 있는 방법이 있다. 
// 함수를 마치 클래스를 만들 듯이 할 수가 있다
// convention은 클래스를 만들 듯이 대문자로 시작하는 대문자 카멜 케이스 방식으로만들고 
// this 키워드를 사용한다. 그리고 인스턴스를 만들 듯이 new로 만들어준다 

const person5 = new Person('Mark', 35);

function Person(name, age) {
    // 여기에서 this는 {} 오브젝트 가 된다
    this.name = name;
    this.age = age;
    // 이것을 리턴하듯이 하는 효과가 된다 즉, return this; 하지만 리턴은 안해줘도 된다
}

console.log(person5);


//// in operator
/// 키가 있는지 확인하는 방법 in을 사용해서 object 안의 키를 확인 할 수 있다
console.log('name' in person5);
console.log("age" in person2);
console.log("gender" in person2);


/// for .. in vs for .. of // c++ 의  item : items 같은 것, 거의 모든 언어에 다 있다
for (key in person5) {
    console.log(key);
}

// for (value of iterable)
// 배열 리스트 (순차적으로 사용할 때)

const array = [1, 2, 3, 4, 5];

for(let i=0; i < array.length; i++) {
    console.log(array[i]);
}
// 이것을 좀더 쉽게 하는 방법은 of 를 사용해주면 된다
for (value of array) {
    console.log(value);
}



/// cloning 
const user = { name: 'ellie', age: 20};
const user2 = user;
console.clear(); /// console 를 지워준다
console.log(user);   // reference 를 복사해주는데 실제 주소를 같이 가리키고 있다 
// 그렇기 때문에 같은 값을 가리키고 있어서 user2 이지만 그 안의 property를 바꾸면 user의 내용도 바뀌게 된다 
// 왜냐하면 같은 곳 (object)을 가리키므로 
user2.name = 'mike';
console.log(user);  // user2의 내용을 바꿨지만 user도 바뀜

// 이런 것 말고 아예 클로닝을 할 수 있는데 
// 먼저 옛날방법이라고 함(아래) -- 직접 할당해준다
const user3 = {};
for (key in user) {
    user3[key] = user[key];
}
console.log(user3);

// object의 assign 을 사용한다. javascript의 모든 오브젝트는 Object를 상속하게 되는데  
// assign() 함수를 사용
const user4 = {}; // 먼저 빈 오브젝트를 만든 후에 assign()을 사용
Object.assign(user4, user)  // assign은 타겟(복사할대상), 소스(원본)이 파라미터
console.log(user4);

// 또는 그냥 바로 리턴을 받으면 된다 
const user5 = Object.assign({}, user);

// assign example -- 여러가지의 오브젝트를 카피하기  
// 공통의 키 가 있지만, 추가된 값이 있는 서로 다른 오브젝트의 경우 
// 뒤에 나오는 오브젝트의 값이 카피가 된다
const fruit1 = { color: "red" };
const fruit2 = { color: "blue", size: "big" }; 
const mixed_fruit = Object.assign({}, fruit1, fruit2);
console.log(mixed_fruit);


