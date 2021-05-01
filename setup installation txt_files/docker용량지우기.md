주의 
용량이 꽉차서 df -h를 해보니
docker가 사용하는 곳이 93%를 사용중;;;; 65기가
Filesystem           Size  Used Avail Use% Mounted on
overlay               70G   65G  5.4G  93% /var/lib/docker/overlay2/f9a60303585c74acb3c301677d7c3465fe5d8e3704f796f01753e6d4fed3b789/merged


지우는 방법은... 근데 이거는 다 지우는 거 이므로;;; 원래 다 지울 생각은 없었는데;; 망 ㅋㅋ
절대 주의!! 뭐 로컬에서 하는것은 지워져도 상관은 없긴한데... 그래도 너무 다 지워버렸네; ㅠ

docker system prune --all --volumes --force
Deleted Containers:
4520d9f063e1037b681b10570d6ef3c647f470f8a239f65b3224ab7fcb2918c8
81fa3df8568205da555f20830363a244bf011754640becc93b0f6617ef1c4f44
923ce86e9f4ca2a3564a5c34781a85693c9f345d92fc26cbae9b3c5a1af5bf07
bcb3de26e90d2ddbffb0d4af74976026837d2ab11508787fb59756cde3cf6003
23964680fe8b575af852a24af9c4eb0545c9cd30c01892f73afa7bc724ed8966

Deleted Networks:
movie-recommendation-api_default
docker-tfod_default
docker-api-test_default
docker-laravel-blog_default
movie-api-docker-git_default
docker-ml_default
docker-streamlit_default

Deleted Volumes:
docker-laravel-blog_mysqldata

...
..
중략..
Total reclaimed space: 54.6GB

사용안하는 컨테이너등 모든 것들을 지움;;;
54기가 확보됨 ;;;

docker ps -a 해보면 아무것도 남아 있지 않다;;




