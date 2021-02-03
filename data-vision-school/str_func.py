firstName = 'Mitch'
lastName = 'Steve'
firstName + lastName
fullName = firstName + ' ' + lastName
fullName.upper()
fullName.lower()
fullName.title()  #한 단어 마다 첫 알파벳은 대문자로 변환

fullName.split() #기본 공백으로 자르기 --> 결과는 리스트로 반환

#파이썬에서 데이터 액세스 기호는 대괄호 []
#변수명 바로 오른쪽에 대괄호
#인덱스는 컴퓨터가 자동으로 매기는 숫자


# 문자열은 immutable 이다. 따라서 한번 생성된 문자열 자체를 바꾸는것은 할 수 없다.
# 따라서, 새로운 메모리에 변경한 문자열을 새로 만드는 방법을 사용하게 된다.


letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
letters[0] = 'k' #0번째를 k로 바꾸라 는 식이지만, 문자열 상수로 바꿀 수가 없다
letters.replace('a', 'k') # 그래서 replace() 메소드 이용

#### 슬라이싱
letters[0:3] #slicing +1을 해준다 , 마지막은 숫자는 포함하지 않음

###** 실무 TIP 슬라이싱 할 때 마지막포함은 +1을 해주는 식으로 처리한다
letters[0:2+1]

letters[:] #전체
letters[-3: ] #마지막 3번째부터 끝까지 
letters[::2] #2개 건너 뛰면서 전체표시

len(letters) #길이 함수


email = 'abc@naver.com'
login = '       abc@naver.com'
email == login
### 공백 제거
login.strip() == login.strip() #공백 제거

poem = "hello world year"
poem.find('year')  #find('str')  문자열의 인덱스 넘버를 반환
poem.rfind('year')  #rfifnd('str') 문자열을 뒤에서 부터 검색해서 인덱스 번호 리턴, #없을 경우 -1을 반환
poem.find('banana') #** find함수는 없으면 -1 반환

#count 함수, 해당 문자열 개수 파악
poem.count('banana') # 없으면 0을 반환

#### in 을 활용해서 문자 찾기 
"banana" in poem # 문자열에서 검색 후 있으면 true, 없으면 false를 반환
