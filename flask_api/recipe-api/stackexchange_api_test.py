import requests
import json
from flask import Flask
#https://api.stackexchange.com/docs/questions

app = Flask(__name__)  # flask 기본구조

# 요청하기, 요청한 응답을  response에 저장
response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

#json형태로 출력
#print(response.json())
for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print("skipped")
    print()

if __name__ == "__main__" :
    app.run()  
