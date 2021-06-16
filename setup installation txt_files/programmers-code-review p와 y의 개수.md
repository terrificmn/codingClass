# 프로그래머스 코딩테스트 연습 리뷰하기
Programmers   

처음 들어본 것은 아니고, 주변에서 눈치로 대충~ 코딩 연습을 하는 것 같은데   
그게 프로그래머스인 것 같았고, 블로그에서도 포스팅 한 것을 봐서 대충 알고는 있었다.

그래서 저번 수업시간 때 처음으로 풀어봤는데  
예전에 처음 프로그래밍 훈련 시작할 때 파이썬 도장으로 별 그리는 코딩을 했었던 것이 생각이 났다

어쨋든 한 일주일 쯤 흘렀을까? 시간이 없어서 정리 못하다가 까먹기 전에 정리를 해야할 것 같아서
포스팅을 해본다~

<br/>

## 문자열 내 p와 y의 개수 문제
프로그래밍 언어는 c++ 입니다~

먼저 문제는 이렇다~

<img src=0>
<br/>


내가 작성한 코드
```cpp
#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    
    int countP = 0;
    int countY = 0;
    
    //cout << s.length();
    for(int i=0; i < s.length(); i++) {
        if(s[i] == 'p' || s[i] == 'P') {
            countP++;
        }   
        
        if(s[i] == 'y' || s[i] == 'Y') {
            countY++;
        }   
    }
    
    if (countP != countY) {
        return false;
    }
       
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;
     
    return answer;
}
```

<br/>

# 코드 리뷰

문자열 s의 길이를 구하는 함수 length()를 이용해서   
s가 들어가 있는 길이 만큼 (문자열은 배열 처럼 구성되어지니깐) for문을 반복해서 

단순하게 s의 문자열에 들어있는 각 문자 하나씩 꺼내서 'p' 와 'P'와 비교하는 방식을 사용했다
마찬가지로 'y'와 'Y'도 마찬가지로 한 후에
countP, countY라는 변수를 만들어서 개수를 저장해줌

마지막으로 서로 몇개인지 확인한 후 다르면 false를 리턴하게 했다



