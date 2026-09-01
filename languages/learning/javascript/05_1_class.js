'use strict';

// 기존의 property, 등을  속성을 fields 라고 부른다 
// ES6 에 추가되었음  

class Person {
    constructor(name, age) {
        // fields -- 속성 member 변수쯤 된다 ㅋ
        this.name = name;
        this.age = age;
    }

    // methods
    speak() {
        console.log(`${this.name}: hello~`);
    }
}

const ellie = new Person('ellie', 30);
console.log(ellie.name);
console.log(ellie.age);
ellie.speak();


class User {
    constructor(first_name, last_name, age) {
        this.first_name = first_name
        this.last_name = last_name;
        this.age = age;
    }
    // getter, setter가 미리 지정되어 있는 예약어 인듯 하다  
    // 그래서 getter는 get(), setter는 set()으로 지정해서 사용하는데 
    // 다른 언어와 조금 다른 부분은 fields 라고 불리는 변수이름으로 함수를 지정하고  
    // 해당 변수 이름으로 값을 주게되면 계속 반복해서 호출이 되는 recursion 에러가 발생 (too much recursion)
    // 그래서 get, set 에서는 해당 클래스의 this.의 변수 이름을 다르게 주는데 
    // 보통 _ (언더스코어)를 넣어서 생성해준다. 예 _age
    get age() {
        // return this.age;
        return this._age;
    }

    set age(value) {

        // this.age = value < 0 ? 0 : value;
        this._age = value < 0 ? 0 : value;
    }
}
const user1 = new User('Steve', 'Job', -1);
console.log(user1.age)



// // private, public
// 비교적 최근에 나왔다고 한다 
// class 안에서 그냥 변수를 선언하면 public으로 만들어지고, # (해쉬)기호를 넣어서 만들면  
// private 이 된다.  

class PublicPrivate {
    publicField = 2;
    #privateField = 0;  // 이렇게 하면 private 으로 만들어진다 
}

const publicTest = new PublicPrivate();
console.log(publicTest.publicField);
console.log(publicTest.privateField);  // private를 내부적으로만 접근할 수 있기 때문에 undefined 로 출력이 된다 

// 2020년 기준으로는 사파리에서는 지원이 아직 안된다고 하는데.. 지금은 되지 않을까 싶다 ㅋ/



///// static
// 함수나 변수 앞에 static 이라고 사용하면 됨

class Article {
    static publisher = "Dream Coding";
    constructor(article_number) {
        this.article_number = article_number;
    }
    
    static printPublisher() {
        console.log(Article.publisher);
    }
}

const article1 = new Article(1);
const article2 = new Article(2);

// static으로 만들게 되면 클래스 자체에서도 메모리에 올라가서 그 값을 사용할 수가 있게 되는데 
// 일반적으로 instance 된 object에서는 호출을 해도 작동을 하지 않는다 
// 클래스 자체를 호출해서 사용할 수 있다. 클래스 자체를 사용하게 된다. (오)
console.log(article1.publisher);

// 클래스 자체에서 호출해야함
console.log(Article.publisher);

// 마찬가지로 그냥 오브젝트에서 함수 메e소드를 호출하면 undefined 라고 나오면 실행이 안된다 
// article2.printPublisher();  // 오히려 function이 아니라고 에러가 발생하게 된다 

// 역시 이것도 클래스 자체에서 호출해야한다
Article.printPublisher();


class Shape {
    constructor(width, height, color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }

    draw() {
        console.log(`drawing : ${this.color}`);
    }
    
    getArea() {
        return width * this.height;
    }
}

// 상속받기~ Inheritance  // 연장한다는 라는 의미의 extends 를 사용 php도 extends 
class Rectangle extends Shape {
}

// 다향성 - 필요한 메소드만 재정의해서 사용할 수가 있다 
class Triangle extends Shape {
    draw() { // 이렇게 하면 새로운 오버라이딩 된 함수가된다 
        console.log("Triangle"); 

        // 부모의 함수를 사용하고 싶을 때에는 super 키워드를 사용한다 
        super.draw();  // 부모의 함수를 사용할 수가 있다
    }
    getArea() {  // 필요한 함수만 지정을 해서 오버라이딩을 overriding을 할 수가 있다  // 부모클래스의 함수를 다시 정의해주면 된다 
        return (this.width * this.height) / 2;
    }
}

const rectangle = new Rectangle(20, 20, "blue");
rectangle.draw();
// 부모 클래스의 draw() 함수를 호출해서 사용할 수가 있다 

const triangle = new Triangle(20, 20, "rea");
triangle.draw();


// 6. instanceOf // 어떤 클래스의 인스턴스, 오브젝트인지 알려준다
// javascript에서는 모든 Object는 'Object' 클래스를 상속받는다
console.log(rectangle instanceof Rectangle);
console.log(triangle instanceof Rectangle);
console.log(triangle instanceof Triangle);
console.log(triangle instanceof Shape);
console.log(triangle instanceof Object);



// MDN의 공식 Javascirpt 메뉴얼을 참고하자!!