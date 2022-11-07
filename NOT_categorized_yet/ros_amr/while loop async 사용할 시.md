ros에서 async 기능을 사용하게 되면 각 함수들은 특히 콜백 함수들은 각각 multi thread로 돌게되어 다 사용을 할 수가 있음

- 단, 서로 각자 돌아서 컨트롤 하기가 어려울 수가 있음
- while loop을 쓰는 경우에는 block이 안 되고 서로 각자 함수에서 thread로 작동하게 된다 
- 하지만 콜백함수 (ros subscribe)가 아닌 경우에는 while loop를 사용하게 되면 block이 되므로 주의해야한다 


