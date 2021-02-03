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


s = ', '.join(['aap', 'bpp', 'cpp'])
print(s)
print('소문자->대문자 변경: ', 'python'.upper())
print('대문자->소문자 변경: ', 'PYTHON'.lower())

#왼쪽 공백 지우기 lstrip()메소드
s = '     PYTHON    '.lstrip()
print(s)
#오른쪽 공백 지우기 rstrip()메소드
s = '     PYTHON    '.rstrip()
print(s)
#공백 지우기
s = '     PYTHON    '.strip()
print(s)
#해당 문자열과 공백까지 제거
s = ' ,python.'.lstrip(' ,')
print(s)
#양쪽의 공백과 특정문자 까지 제거 
s = ' ,python. '.strip(' ,. ')
print(s)
print("-----------------------------")

s = 'python'.ljust(10)
print(s)
s = 'python'.rjust(10)
print(s)
s = 'python'.center(10)
print(s)
s = 'python'.rjust(10).upper()
print(s)

s = 'apple pineapple'
#특정값을 찾아서 index 반환 (처음 찾은거 해당)
print(s.find('pl'))
#rfind()메소드는 오른쪽부터 찾음 (현재pl 문자열이 2개가 겹침)
print(s.rfind('pl'))
#? find()메소드로 문자열을 못찾게되면 -1을 반환한다
print(s.find('xy'))
print(s.index('pl'))
#** index메소드도 문자열을 찾아주나 find()와 다르게 문자열이 없으면
#** 에러가 발생한다. find()은 -1 반환 
#** 에러가 발생하므로 index()도 유용할 수 있다
# print(s.index('xy'))  #없다면 에러 발생 
#count()메소드는 문자열을 찾아서 개수를 반환
print(s.count('pl'))

#** % 매칭
#** %s = 문자열, %d는 integer, %f는 float

print('I am %s' % 'James')
#%s의 s앞에 숫자를 넣어주면 정렬의 효과
print('I am %10s' % 'James')
#%s의 s앞에 -숫자를 넣어주면 왼족 정렬의 효과
print('I am %-10s' % 'James')
#int형은 %d int형과 매칭
print('I am %d year old' % 20)
print('I am %f weight' % 60.5)
#float형은 f앞에 숫자를 적어주면 숫자만큼 소수점 표시하게 됨
print('I am %.2f weight' % 60.5)
#여러개 처리 %(value, value) 콤마로 구분
print('Today is %d %s' %(19, 'Jan.'))
#여러개 처리 예:
nbr1, nbr2 = 3.5, 20.5
nbr1 = float(nbr1)
nbr2 = float(nbr2)
multiplication = nbr1 * nbr2
addition = nbr1+ nbr2
print("First is %.1f, and second is %.2f. So, Multiplication = %.3f, addition = %.2f" % (nbr1, nbr2, multiplication, addition))
# format()
print("First is {}, and second is {}. So, Multiplication = {}, addition = {}".format(nbr1, nbr2, multiplication, addition))


#? formatting은 문자열안에 중괄호{}를 format(value값)으로 넣어준다
#? {}중괄호 안에는 인덱스 번호를 넣어준다
print('Hello {0}'.format('world'))
print('Hello {0}'.format(100))
print('Hello, {0}, {1}, {2}'.format('world','script', 3.8))
#{안의}인덱스와 일치하지 않으면  arguments가 많다고 warning발생
print("Hello {0} {0} {1} {1}".format('world', 'script', 3.8))
#인덱스를 생략하면 자동으로 순서대로 바꿔줌
print("Hello {} {} {}".format('world', 'script', 3.8))
print("----------------------------------------")

#?변수형태로도 문자열안의 변수를 바꿔서 출력가능
print('{str1}, {str2} 3.6'.format(str1='Hello', str2='Python'))

lan = 'python'
ver = 3.9
#?처음에 print로 출력할 때 ()안에 f를 넣고 시작 
print(f'Hello {lan} {ver}')

#정렬 
#왼쪽으로 정렬 {}로 묶고, 0:<10이면 왼쪽으로 먼저 출력 후 나머지 오른쪽 공간을 채움
print('{0:@<10}'.format('python'))
#오른쪽으로 정렬 {}중괄호로 묶고, 0:>10이면 
print('{0:@>10}'.format('python'))
print('{0:>10}'.format('python'))

#오른쪽으로 정렬, 0부터, 4f 는 소수점 4자리
print('{0:>12.4f}'.format(1675.3))
#똑같은 방식 (0생략 가능)
print('{:>12.4f}'.format(1675.3))
#3자리 마다 ,를 찍어준다 

print(format(123456789,","))








