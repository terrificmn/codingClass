'use strict'
// make a string out of an array
{
    const fruits = ['apple', 'melon', 'strawberry'];
    let result = fruits.join();
    console.log(result);
    //join을 사용하면 파라미터를 생략할 수도 있고 이럴 경우에는 ,을 자동으로 삽입해준다
    // join은 배열의 요소를 하나씩 합쳐서 문자열로 만들어준다

    result = fruits.join(', ');
    console.log(result);
}

// make an array out of a string
{
    const fruits = "banana, apple, melon";
    let fruits_array = fruits.split(', ');
    console.log(fruits_array);
    fruits_array = fruits.split(', ', 2);  // 두 번째 파라미터는 optional 이지만, 몇번째 요소까지 할지 limit을 정할 수가 있다
    console.log(fruits_array);
}

// make this array look like this: [5, 4, 3, 2, 1]
// 거꾸로 뒤집기
{
    const array = [1, 2, 3, 4, 5];
    const result = array.reverse(); // reverse는 원래 바꾸려고 했던 원본도 바꿔준다
    console.log(result);
    console.log(array); // 이것도 바뀌어짐
}

// make new array whithout the first two elements
{
    let array = [1, 2, 3, 4, 5];
    // splice()
    let new_array = array.splice(0, 2); // 새롭게 만들어주지만, 원 데이터도 바뀐다
    console.log(new_array);
    console.log(array);

    array = [1, 2, 3, 4, 5];
    // slice()
    // 파라미터에 넘어가는 number는 index를 의미,
    // 2번째 파라미터는 end 인데, 마지막 요소 index를 exclusive 한다고 되어 있으므로 +1을 해서 넣어줘야 원하는 만큼 slice가능
    // 생략가능
    // 원본은 그대로 있다
    new_array = array.slice(2, 5);
    console.log(new_array);
    console.log(array);
}


class Student {
    constructor(name, age, enrolled, score) {
        this.name = name;
        this.age = age;
        this.enrolled = enrolled;
        this.score = score;
    }
};
const students = [
    new Student('Mike', 29, true, 59),
    new Student('Mark', 22, false, 39),
    new Student('John', 23, true, 97),
    new Student('Kate', 25, false, 79),
    new Student('Lisa', 32, true, 89)
];

///// 12:07 차례임
