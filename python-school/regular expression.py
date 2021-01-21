#정규식 모듈 import 하기 (모듈명은 re)
import re

#match('패턴문자열', '찾을대상문자열')
#일치하면 match='패턴문자열' 이라고 출력된다
print(re.match('hello', 'hello world'))
#match는 무조건 시작 단어에서만 찾는다 -그래서 아래의 코드는 None이라고 못찾았다고 나옴
print(re.match('world', 'hello world'))
#반면에 search는 시작 끝 상관없이 찾는다
print(re.search('hello', 'hello world'))
print(re.search('world', 'hello world'))

#match에 | or조건을 넣어주는것도 가능
print(re.match('hello|world', 'hello python'))

# []대괄호의 패턴문자열은 0-9면 숫자이고 *의 의미는 0개 이상
print(re.match('[0-9]*', '1234'))
# []대괄호의 패턴문자열은 0-9면 숫자이고 +의 의미는 1개 이상
print(re.match('[0-9]+', '1234'))

#아래의 결과는 1개의 이상의 숫자가 없으므로 None을 반환
print(re.match('[0-9]+', 'abc'))

# ^는 시작의 의미 즉, 시작을 hello인지 확인
print(re.search('^hello', 'hello world'))
# $는 끝의 의미 즉, 끝이 world인지 확인
print(re.search('world$', 'hello world'))

#. ?는 0개 또는 1개, 찾는 문자열에서 h뒤에 붙은 단어가 0개 또는 1개
print(re.match('h?', 'h'))

# .은 패턴문자열 뒤에서 무조건 1개 와야함
print(re.match('h.', 'h'))  #결과는 None 
print(re.match('h.', 'hi')) #결과는 match

# {}중괄호는 갯수를 지정 숫자는 바이트?
print(re.match('[0-9]{3}', '123'))
print(re.match('[0-9]{3}', '12'))  #결과는 None

# {}중괄호에 ,(comma)를 찍으면 2바이트 또는 3바이트 의미
print(re.match('[0-9]{2,3}', '123'))
print(re.match('[0-9]{2,3}', '12'))
print(re.match('[0-9]{2,3}', '1'))  #결과는 None
print(re.match('[0-9]{2,3}', '1234'))


print(re.match('h{3}', 'hhhello')) #h를 3번, 찾는 문자열에서 h가 3번 연속으로 있어서 match
print(re.match('h{3}', 'hhello')) #h를 3번, 찾는 문자열에서 h가 연속으로 3번없어서 None
print(re.match('(hello){3}', 'hhhhello')) #hello가 3번 찾음, None
print(re.match('(hello){3}', 'hellohellohelloworld'))

#전화번호 정규식 
print(re.match('[0-9]{3}-[0-9]{3,4}-[0-9]{4}','010-1234-1234')) #패턴 match
print(re.match('[0-9]{3}-[0-9]{3,4}-[0-9]{4}','010-124-1234')) #패턴 match
print(re.match('[0-9]{3}-[0-9]{3,4}-[0-9]{4}','010-12-1234')) #패턴 None (중간 숫자가 2자리 이므로)

#. 마지막 *은 0개 이상
print(re.match('[a-zA-Z0-9]*', 'hello1234'))
print(re.match('[a-zA-Z0-9]*', '한글')) # , *로 처리가 되어있어 0개 이상이어서 None 나오지는 않는다

# +는 1개 이상
print(re.match('[a-zA-Z0-9]+', 'hello1234'))
print(re.match('[a-zA-Z0-9]+', 'h')) #한개 있으므로 match
print(re.match('[a-zA-Z0-9]+', '')) #한개도 없으므로 None
print(re.match('[a-zA-Z0-9]+', '!!@')) #특수기호는 정규식에 없으므로 None


#! []대괄호 안에 ^을 넣으면 시작의 의미가 아니고 not 의미가 됨 
print(re.match('[^0-9]{2,3}', '123'))  #숫자가 아닌것을 찾아라는 의미이므로 찾을 대상은 숫자밖에 없으므로 None 반환
print(re.match('[^0-9]{2,3}', 'abc'))  #숫자가 아닌 문자가 있으므로 match

print(re.match('[^a-z]+', 'hello'))  #소문자가 아닌것을 찾으므로 None
print(re.match('[^A-Z]+', 'hello'))  #대문자가 아닌것을 찾으므로 match
#! []대괄호 전에 ^을 사용하면 시작의 의미이다 
print(re.match('^[0-9]+', 'Hello'))  #시작을 숫자로 하는것을 찾으므로 None

#숫자이며 + 1개 이상으로 $ 끝나는것 찾기
print(re.match('[0-9]+$', 'hello1234')) #match 함수는 시작만 찾으므로 None
#제대로 된 값을 볼려면 search()함수를 사용 (#숫자이며 + 1개 이상으로 $ 끝나는것 찾기)
print(re.search('[0-9]+$', 'hello1234')) #search 함수는 전체에서찾으므로  끝나는것 숫자 match

#? 순수 *표시를 찾고 싶을 때는 이스케이프를 \를 *앞에서 해준다 \*
#아래코드는 *(0개이상)+(1개이상)이므로 논리오류가 난다
#print(re.search('*+', '1**2'))
#이런경우에는 escape를 해줌 , 그러면 *을 정규식이 아닌 특수기호로 인식
print(re.search('\*+', '1**2'))

# $  (  ) 등의 특수기호는 이미 언어에서 사용하고 있는 것이기 
# 때문에 순수특수기호를 인식하게 하려면 이스케이프문자 \를 사용해야하는데
#! []대괄호 안에서 사용하면 그냥 사용해도 특수기호로 인식한다
print(re.match('[$()a-zA-Z0-9]', '$(dodcument)'))
print(re.search('[*]+', '1**2')) #대괄호 안에서는 특수기호로 인식
print(re.search('\*+', '1**2')) #대괄호가 아닐 때는 \를 넣어줘야함(이스케이프) 여기서 \를 안하게 되면 아예 오류가 남

#공백문자 \s 
print(re.search('[a-zA-Z0-9\s]+', 'hello world spacebar'))
print(re.search('[a-zA-Z0-9\s]+', ' ')) # 공백 match

#그룹화 하기 괄호로 묶어서 그룹화 하고 반드시 그룹사이에는 반드시 공백을 넣어야함 
# 예 ([정규식])([정규식]) 안됨
# 예 ([정규식]) ([정규식]) 오키
m = re.match('([0-9]+) ([0-9]+)', '10 259')
print(m.group(1)) 
print(m.group(2))
print(m.group()) #그룹 전체 보기

# []대괄호는 한글자에 대한 정규식 []+ 이면 1글자 이상 (여러글자가 됨)
#! 그룹이름을 지어주는 것은 ?P<그룹이름> 이렇게 약속되어 있음 
# 그리고 나서 group()함수로 숫자가 아닌 이름을 쓸 수 있다 (그룹이름을 지정 안하면 숫자 1, 2, 3 이런식으로 됨)
m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
print(m.group('func'))
print(m.group('arg'))

#찾는 주어진 문자열에서 문자열을 바꿔주는 함수 sub()
#1번은 찾을 문자열 , 2번은 바꿀 문자열,  3번은 주어진 문자열 -- 매칭이 되면 바꿔 준다
# | 은 or
print(re.sub('apple|orange', 'fruit', 'apple box orange tree'))
# 한자리 이상의 숫자가 있으면, n으로 바꿈 , 대상주어진문자열에서 
print(re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8'))



