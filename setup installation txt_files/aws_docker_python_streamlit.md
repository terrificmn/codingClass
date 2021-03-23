# AWS 에 Docker로 streamlit 셋팅하기

## docker 설치
먼저 docker를 설치해야하는데, `docker설치하기_dockerfile설명.md` 를 참고한다
하나 문제는 aws 프리티어가 1GB램인가 밖에 안되서 메모리 문제가 발생
`메모리swap하기.md` 파일 참고할 것
그외는 매뉴얼 페이지를 그대로 따라하면 거의 문제 없이 설치된다.

그리고 나서 Dockerfile, docker-compose를 만든는데, 
`python정리버전.md`을 다운받거나 복사해서 만들던가 상관없음

## git에서 프로젝트 pull하기
streamlit으로 돌릴 프로젝트들을 app 디렉토리안에 하나씩 설치해준다
8501포트는 app/ 디렉토리 안에 app.py가 실행되게 되어 있고
그리고 나머지 8502 부터는 app/new_app  이런식으로 하위 디렉토리를 만들어서 두 번째 프로젝트 (app.py)를 넣어주면 됨



