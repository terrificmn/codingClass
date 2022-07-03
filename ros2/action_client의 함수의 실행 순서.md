## Action Client의 callback 함수 설명 및 실행 시점


send_goal 함수를 을 먼저 수행을 하고 goal send에 feedback_callback이 묶이며 send_goal이 완료되는 시점에 
goal_response_callback으로 이동

goal_response_callback은 get_result_async가 완료되는 시점에 get_result_callback으로 이동하게 됨

feedback_callback 함수는 지속적으로feedback을 출력하게됨

get_result_callback 함수는 최종적으로 마지막에 실행되는 함수이며 Result를 출력하게 됨


py_action패키지의 action-client.py 파일을 참고한다

