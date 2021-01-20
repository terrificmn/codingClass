'''
#연습문제
file = open('words.txt', 'w')
file.write('anonymously\ncompatibility\ndashboard\nexperience\nphotography\nspotlight\nwarehouse\n')
file.close

with open ('words.txt', 'r') as file:
    count = 0
    txtLines = file.readlines()

    for i in txtLines:
        if len(i.strip('\n')) <= 10:
            count += 1

print(count)
'''

f = open('words.txt', 'w')
f.write('Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.')
f.close

with open ('words.txt', 'r') as f:
    #! readlines()메소드로 하면 split()를 사용할 수 없음에 주의
    # readline() 으로 해야함 한 줄 
    lines = list(f.readline().split())

    #print(lines)    
    for i in lines:
        #find메소드 인덱스 값을 넘겨줌, 없으면 -1 반환
        if i.find('c') >= 0:
            print(i.strip(',.'))


