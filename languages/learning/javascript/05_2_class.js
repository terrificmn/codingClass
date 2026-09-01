class Counter {
    constructor() {
        this.counter = 0;
    }

    increase() {
        this.counter++;
        if(this.counter % 5 == 0) {
            console.log(`counter: ${this.counter}`);
        }
    }
}

// new 키워드로 만들어 준다.
const myCounter = new Counter;
myCounter.increase();
myCounter.increase();
myCounter.increase();
myCounter.increase();
myCounter.increase();

console.log("---------------------------");

// 여기에서 콜백함수를 increase() 함수에 넘겨서 실행하게 할 수도 있다.
// 여기에서 콜백함수를 increase() 함수에 넘겨서 실행하게 할 수도 있다.
class Counter2 {
    constructor() {
        this.counter = 0;
    }

    // 확실히 함수를 따로 정의를 하지 않기 때문에 헤깔릴 수 있지만 차근차근 잘 찾아가야 한다. 
    increase(run5Times) {  // run5Times 라는 파마리터를 만들어서 myPrint()함수를 받는다. 
        this.counter++;
        console.log(`counter2: ${this.counter}`);
        if(this.counter % 5 == 0) {
            run5Times(); // run5Times 는 인자로 받은 myPrint()함수가 실행되는 것
        }
    }
}

function myPrint() {
    console.log("every 5 times reached!!!!!");
}
function myAlert() {
    alert("alert: 5 times reached!!!!!");
}

// new 키워드로 만들어 준다.
const myCounter2 = new Counter2;
myCounter2.increase(myPrint);
myCounter2.increase(myPrint);
myCounter2.increase(myPrint);
myCounter2.increase(myPrint);
myCounter2.increase(myPrint);
myCounter2.increase(myPrint);
myCounter2.increase(myPrint);
myCounter2.increase(myPrint);
myCounter2.increase(myPrint);

// 함수 자체를 넘겨주므로, 새로운 함수를 만들어서 그것을 실행할 수 있게 할 수 있다. 
// 예를 들어서 myPrint를 넘겨주다가. 5번 마다 넘겨준 myPrint가 실행이 되는 것인데, 10번째에는 다른 함수를 만들어서 넘겨주면 다른식으로 작동하게 할 수 있게 된다.
myCounter2.increase(myAlert);   /// 10번째에는 다른 함수를 넘겨서 작동하게 할 수가 있다.



// class 에서는 constructor에서 처음에 할당을 해서 만들어 주는 방식이 많이 사용된다.
// constrctor에서 파라미터로 받아서 미리 콜백함수를 셋팅한다.
class Counter3 {
    constructor(myPrint) {
        console.log("Counter3 created");
        this.counter = 0;
        this.myCallbackMyPrint = myPrint; /// 함수로 들어온 것을 클래스 내에 변수 할당
    }

    increase() { 
        this.counter++;
        if(this.counter % 5 == 0) {
            this.myCallbackMyPrint(); // 클래스의 myCallbackMyPrint()는 인자로 받은 myPrint()함수가 실행되는 것
            console.log(`counter3: ${this.counter}`);
        }
    }
}

// new 키워드로 만들어 준다.
const myCounter3 = new Counter3(myPrint);  /// myPrint() 함수를 넘겨준다. 컨스트럭터에서 해당 함수로 할당
myCounter3.increase();
myCounter3.increase();
myCounter3.increase();
myCounter3.increase();
myCounter3.increase();

// 확실히 선언부가 따로 없으니 각 클래스등에서 변수이름이 다르게 하면 상당히 헤깔릴 듯 하나, 차근차근 보는 것이 중요할 듯 하다.
