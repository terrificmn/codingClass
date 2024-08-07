let myButtonController = null;


function load() {
    myButtonController = new MyButtonController('button1', 'button2');
    // 보통 클래스 내의 함수들을 보통적인 방법으로 접근해서 호출 할 수가 있다.
    myButtonController.testPrintA()
}

// 클래스
class MyButtonController {
    // html의 button 의 id 값을 받아와서 id 등록 및 event callback함수로 등록
    constructor(button_1, button_2) {
        this.button1 = document.getElementById(button_1);
        this.button2 = document.getElementById(button_2);

        /// clickButton1, clickButton2 함수는 addEventListener()로 콜백함수로 묶여 있기 때문에 그냥 사용을 하면 clickButton1/2 함수를 찾지 못한다.
        /// 이를 위해서 bind() 함수로 한번 더 현재 클래스의 주소를 알려주고, 
        /// 또 다른 방법으로는 this 키워드로 콜백함수를 지정하고나서 arrow function을 이용해준다..clickButton2 를 참고
        this.button1.addEventListener('click', this.clickButton1.bind(this), false);
        // bind 대신에 다른 방법 사용, 함수쪽에서 ()=> arrow functions 이용 (참고, bind와 같은 효과)
        this.button2.addEventListener('click', this.clickButton2, false); 
    }

    // 보통 함수를 지정할 때 function 키워드를 사용했지만 클래스 내에서는 function 키워드를 사용하지 않는다. 
    testPrintA() {
        console.log("this is testPrintA()");
        /// 클래스내에서 함수를 사용할 경우에는 this 키워드를 사용해서 접근해줘야 한다.
        // 그렇지 않으면 testPrintB()는 testB is not define 이라는 에러를 발생시킨다.
        this.testPrintB();
    }
    testPrintB() {
        console.log("test. now testPrintB()!");
    }

    /// clickButton1, clickButton2 함수는 addEventListener()로 콜백함수로 묶여 있기 때문에 그냥 사용을 하면 
    /// 클래스 안의 clickButton1/2 함수를 잘 연결되지만 addEventListener() 에서 this.함수이름 으로 지정되어 있다면 해당 함수가 잘 실행은 되지만
    /// 해당 함수에서 클래스 내의 다른 함수 호출이 안된다. 이는 현 클래스의 주소를 지정이 안되서 문제가 발생한다. (다른 함수 호출이 안된다.)

    /// bind()함수로 지정했다면 그냥 보통 함수처럼 사용할 수가 있다.
    /// this 키워드가 잘 작동하게 된다. 
    clickButton1() {
        this.testPrintB();
        console.log("button1 clicked.");
    }
    
    /// bind() 방식 외에 다른 방법으로는 arrow function operator를 사용하는 것인데 아래와 같은 방식으로 사용하면 된다.   
    /// ES6 이상에서 사용 가능한 방식이며, class 인스턴스와 메소드를 자동으로 bind 해주게 된다.
    clickButton2 = () => {
        console.log("button2 clicked.");
    }
    
}

//  처음 브라우저 window 에 실행되면서 load 함수를 등록해서 실행
window.addEventListener('load', load, false);