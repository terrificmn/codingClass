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

/// find a student with the score 90
{
    // find() 함수를 찾아보면 함수를 만들어서 그 안에 변수를 넣어주면 된다
    // 함수를 만들어서 넘길 때 boolean을 리턴해줘야한다 -- true면 멈추게 된다
    const result = students.find( function(student, index) {
            console.log(student, index);
            return student.score >= 90;   // true가 되면 리턴이 된다.
        });
    console.log(result);
}

// 위에 것을 function()을 해서 사용을 할 때 => 애로우키를 이용해서 사용할 수가 있다
// find는 배열에 있는 것을 한번씩 콜백을 해준다 
// 한줄로 만든다면 콜백 함수에 => 뒤에 {} 컬리브래킷을 생략할 수 있고, 한 줄이라면 return 도 가능하다
// students.find( (student) => student.score === 39 );  // 이런식

{
    const result = students.find( (student) => {
        return student.score == 39;
    })
    console.log(result);
}


/// make an array of enrolled students
/// filter 이용하기~ 이것도 콜백함수를 만들어서 넘겨줘야 하는데, 
/// 배열마다 한번씩 접근을 해서 함수를 콜 해주기 때문에 콜백 함수라고 하는 듯 하다 
/// filter함수에서 한번씩 콜백을 하면서 전체 인덱스중에서 n번째 배열의 값을 student로 해서 넘겨주게 된다.
/// value, item 이런식으로 많이 사용함. 일단 naming convention이 하나의 객체를 복수형으로 만들고   
/// 거기에서 나오는 것을 단수형으로 만들면 좀 더 편하다. students - student, items - item
{
    const result = students.filter( (student) => {
        return student.enrolled; 
    });

    console.log(result);
}

/// make an array containing only the students' scores
/// map 함수는 콜백함수를 만들어서 넘겨주면 그 값을 새로운 값으로 매칭해서 새롭게 배열을 만들어 준다 
/// 배열 안에 있는 모든 값들을 콜백함수를 통해서 그 파라미터로 맞춰서 다시 넘겨주게 되고 
/// 그 콜백 함수안에서 처리를 한 값을 리턴을 받아서 새로운 배열을 만들어 주게 된다 
// 예제에서는 score만 받아서 return을 하므로 score로만 이루어진 배열이 만들어 진다
{
    const result = students.map( (student) => {
        return student.score;
    });
    console.log(result);
    // 이 역시 한줄로 하면 return 및 컬리 브래킷을 생략할 수 있다
    let new_result = students.map( (student) => student.score );
}


/// check if there is a student with the score lower than 50

{
    /// 여기에서는 some()은 하나라도 조건에 맞는다면 리턴이 true가 된다
    let result = students.some( (student) => {
        return student.score < 50;
    });
    console.log(result);

    /// every() 함수는 모든 배열의 조건이 다 맞아야만 true를 반환한다
    result = students.every( (student) => {
        return student.score < 50;
    });
    console.log(result);
}

/// compute students' average score
/// reduce 배열의 모든 값을 누적해서 리턴하게 되는 함수
{
    // 첫 번째 파라미터에는 current로 넘어간 값이 prev 값으로 들어가지게 된다
    const result = students.reduce( (prev, current) => {
        console.log('----------');
        console.log(prev);
        console.log(current);
        // return current;
        return prev + current.socre;
    })
}

31;04  reduce 함수 다시 한번 보기