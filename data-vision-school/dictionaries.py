my_dict = {'data1':500,
          'data2':-10,
          'data3':300}
# dictionary 에서 value 더하기
sum(my_dict.values())  #sum을 하면 for문을 안하고 바로 다 더 할 수 있음
#values()는 모든 values를 반환 

student_details = [
  {'student_id' : 1, 'subject' : 'math', 'midterm' : 60, 'final' : 85},
  {'student_id' : 2, 'subject' : 'math', 'midterm' : 80, 'final' : 78},
  {'student_id' : 3, 'subject' : 'math', 'midterm' : 90, 'final' : 85}
]

#위의 student_details는 리스트안에 딕셔너리가 들어간것에 유의!
# 그래서 [0]번째의 딕셔너리 키값으로 접근 해야함
student1 = (student_details[0]['midterm'] + student_details[0]['final']) / 2 #평균구하기 
student2 = (student_details[1]['midterm'] + student_details[1]['final']) / 2
student3 = (student_details[2]['midterm'] + student_details[2]['final']) / 2


#평균점수 'average'키로 추가하기
student_details[0]['average'] = student1
student_details[1]['average'] = student2
student_details[2]['average'] = student3
#마찬가지로 리스트안에 딕셔너리로 되어 있으니, [인덱스]로 먼저 접근


my_salary = {"alex": 25, "sally": 28, "dina": 30}
#딕셔너리의 모든 값 더하기

#  keys()메소드는 모든 키만 가져옴
key_list = list(my_salary.keys()) #list()로 만들기

# values()메소드는 모든 값만 가져옴
value_list = list(my_salary.values())

#딕셔너리 길이 구하기
my_dict = {"sally": 23, "dina": 22, "holy": 50, "Joe": 10, "Peter": 44}
len(my_dict)

#정렬하기 
sorted(my_dict.values())



