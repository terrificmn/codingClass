#* 문자열 조작 methods

#*문자열 바꾸기
#replace('특정str', '바꿀str')메소드는 각 arguments를 각각 바꿔준다
a = 'hello, world'
print(a.replace('world', 'Python'))

#* 문자열 분리
#split('기준문자열')
string = 'apple pear grape pineapple orange'
#split()에 문자열을 넣지 않으면 공백을 기준으로 리스트를 만들어준다
#(,)콤마로 넣어짐
print(string) #기존 그냥 문자열에서 
print(string.split()) #리스트로 바뀜

stringcomma = 'apple, pear, grape, pineapple, orange'
print(stringcomma) #쉼표가 들어가 있는 문자열에서 
#? split('기준str') 을 넣어주게되면 해당문자열을 기준으로 분리시켜 리스트로 만듬
print(stringcomma.split(', ')) 



