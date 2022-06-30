git 로컬파일 overwrite 하기

!! 매우 주의!!

git pull origin main 할 때 로컬 파일들이 있는 상태에서 git init을 하면
remote repo에서 pull 하게 되면 겹치는 파일들을 제거 한후 다시  pull을 하라고 나온다
현업에서는 이런일이 없겠지만;; 아마도? 

아직 라라벨을 완벽하게 모르겠는데 깃 허브에 올려서 집, 학교에서 작업하다 보니
학교에서 pull을 해서 작업을 하고 싶은데..;
라라벨을 일단 뉴 프로젝트를 해서 다운을 받아야하는데 
(프로젝트를 애초에 push할 때 gitignore에 의해서 모듈 및 파일 등이 다 안올라간 상태에서
작업한 것이라서, 아무것도 없는상태에서 git init을 하고 pull 하게 되면은 충돌은 없겠지만
실행이 안됨 ㅋㅋㅋ)

그래서 일단 라라벨 프로젝트를 만들고 pull을 받는데 
git pull myblog main   << remote을 myblog로 설정해놓은 것, main은 master라고 안하고 main으로 함
역시나 충돌
error: The following untracked working tree files would be overwritten by merge:
... 파일들..
Please move or remove them before you merge.
Aborting

이제부터는 주의!!
로컬에서 바뀐게 있다면 다 반영안된다. (커밋기준) 근데 untracked이면 그런 파일은 상관없음
그리고 나면
$ git fetch --all  <<<< 최신으로 업데이트됨 (리모트 리포로부터 최신을 다운로드하지만 merge / rebase를 안함)
그러면 Fetching myblog 라고 뜸, 이상태에서는 변한것은 없음
$ git checkout -b backup-main  <<< 백업용 만들기 브랜치 만들기 (사실은 git을 막 init한 상태라 브랜치가 없다? 그래서 하나만 생김
backup-main으로 생김, 그래서 백업의 의미로 쓸려면 브랜치를 하나 더 만들어야하는 듯)
$ git reset --hard myblog/main  << 리모트 리포 등록한 이름과 리모트 브랜치를 적어준다. 정석은 myblog가 origin
이제 reset은 리모트로부터 fetch한 것으로(다운로드받은것을) 바꾼다.
그리고 --hard옵션은 현재 로컬의 워킹트리에 있는 파일들을 리모트 리포지터리의 myblog/main의 파일로 바꿔주게 됨

HEAD is now at 05b4eef first updated blog 이라고 나오면서 
파일들이 생긴다 (드디어 원격과 같아짐)

git branch -m main ....> 다시 main으로 바꾸기



아래 설명
Explanation:

git fetch downloads the latest from remote without trying to merge or rebase anything.

Then the git reset resets the master branch to what you just fetched. The --hard option changes all the files in your working tree to match the files in origin/master
Maintain current local commits

[*]: It's worth noting that it is possible to maintain current local commits by creating a branch from master before resetting:

git checkout master
git branch new-branch-to-save-current-commits
git fetch --all
git reset --hard origin/master

After this, all of the old commits will be kept in new-branch-to-save-current-commits.


_____________________________________________________________________________________________________

파일을 실수로 올렸을 경우에는 해당파일을 지우더라도 히스토리에 남아서 언제든지 깃허브에 들어가면
다시 볼 수 있다. 해당 히스토리에서 Load diff 를 보면 지워졌던 내용도 보인다 ㅠ
뭔가 복구를 할 때는 정말 좋은 시스템이기는 하다, 하지만 노출되면 안되는 파일이 올라가면...
올라가면 치명적이게 된다;; ㅠㅠ 

어쨋든 히스토리에도 삭제하는 방법이다. git filter-branch 명령어를 사용한다

[깃허브 매뉴얼](https://docs.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository)

중요! 먼저 하기전에 깃허브 매뉴얼에서도 이미 깃 허브에 커밋이 되었다면 (push까지) 노출이 되었으므로
비번은 바꾸고, 키를 만들었으면 새로 만들라고 한다!!

뭐.. 학습용이니 누가 볼까하지만서도 그래도 바꾸고 시작하는것도 좋을 듯하다


1. 먼저 다른 곳에 temp같은 디렉토리를 만들고 클론, (백업 목적) 을 해준다
```
$git clone MY-GIT-HUB-REPO.GIT
```

2. 그리고 문제가 있는 로컬의 디렉토리로 이동
```shell
$cd ~/Projects
```

3. 삭제시키는 명령어 적용
강제로 진행하고, 특정 파일(경로/파일명)을 지우고, tags도 덮어씌운다
```shell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch flask_api/recipe-api/config/config.py" --prune-empty --tag-name-filter cat -- --all
```
문제였던 파일이 flask_api/recipe-api/config/config.py 처럼 문제가 된 파일을 잘 써준다

원래 매뉴얼에 나와있는 명령어 참고
```shell
 $git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH-TO-YOUR-FILE-WITH-SENSITIVE-DATA" \
  --prune-empty --tag-name-filter cat -- --all
  > Rewrite 48dc599c80e20527ed902928085e7861e6b3cbe6 (266/266)
  > Ref 'refs/heads/main' was rewritten
```

4. 리다이렉트 기능을 이용해서 .gitignore에 추가해준다. 
```shell
$ echo "YOUR-FILE-WITH-SENSITIVE-DATA" >> .gitignore
```

나의 경우는 
```shell
$ echo "flask_api/recipe-api/config/config.py" >> .gitignore
```

5. 위의 깃 이그노어 파일을 add, commit을 해준다 
```shell
$ git add .gitignore
$ git commit -m "add dir/file to .gitignore"
```


6. 강제 push를 한다. 내 컴터 로컬 변화를 깃허브 리포지터리에 덮어씌운다.
```shell
$git push origin --force --all
```

다른 코워커가 있다면 rebase를 해야한다고 한다. merge를 하면 안되고, rebase를 해보긴 했으나 
아직 정확히 잘 모르겠다;; 공부가 더 필요
그리고 혼자서 하는 중이니 해당사항 없음. 

결과: 다시 깃허브에서 해당 리포지터리를 들어가서 커밋이력을 보게되면
해당 내용이 아예 안나오게 된다!

좋은 공부가 되었다.. 깃 이그노어를 잘 사용하자;;
잘 사용했었는데.. 서둘러서 commit하면 안되겠다.. 


_____________________________________________________________________________________________________
깃 커밋 잘못했을 때 커밋 취소하기
이그노어를 수정한다음에 커밋을 했는데 용량 큰거를 뺀다고 한게 data디렉토리를 누락시켰다.
알고 봤더니 용량이 꽤 컷다..
그래서 push를 할 때 에러가 발생~ ssl 에러가
error: RPC failed; curl 55 OpenSSL SSL_write: SSL_ERROR_ZERO_RETURN, errno 32
fatal: the remote end hung up unexpectedly
Writing objects: 100% (82/82), 252.69 MiB | 15.38 MiB/s, done.
Total 82 (delta 3), reused 0 (delta 0), pack-reused 0
fatal: the remote end hung up unexpectedly


그래서 git log를 확인한 후에 git reset으로 취소시킨다
아래를 보자


```
(base) [sgtOcta@localhost src]$ git log
commit e4ec9a3702c28d4ab1c4a879c387edecd5326d64 (HEAD -> main)
Author: terrificmn <mildsm@gmail.com>
Date:   Fri Apr 30 17:24:00 2021 +0900

    complete except video

commit 645e2fd1f83992f84d92d78e602b8de9020465c1 (tfod/main)
Author: terrificmn <mildsm@gmail.com>
Date:   Tue Apr 27 16:32:31 2021 +0900

    Dockerfile yml requirements file removed

commit 97f2088e95cf80b77cd5dd59056056b35ff0bd07
Author: terrificmn <mildsm@gmail.com>
Date:   Tue Apr 27 14:13:55 2021 +0900

    first commit
(base) [sgtOcta@localhost src]$ git reset --soft HEAD~1
```
그리고 다시 git log를 확인해보면
마지막에 했던 커밋이 취소되어 있다 

커밋은 취소되었지만.. 이그노어가 제대로 반영이 안된다..

일단 git status
를 해보면

```
	modified:   .gitignore
	new file:   Dockerfile
	modified:   app.py
	new file:   data/coco_classes.txt
	new file:   data/images/logo/anaconda_logo.png
	new file:   data/images/logo/awsec2_logo.png
	new file:   data/images/logo/centos_logo.png
	new file:   data/images/logo/docker_logo.png
	new file:   data/images/logo/git_logo.png
	new file:   data/images/logo/github_logo.png
	new file:   data/images/logo/opencv_logo.png
	new file:   data/images/logo/python_logo.png
	new file:   data/images/logo/streamlit_logo.png
	new file:   data/images/logo/tensorflow_logo.png
	new file:   data/images/logo/ubuntu_logo.png
	new file:   data/images/show/boxed.jpg
	new file:   data/images/show/children-640.jpg
	new file:   data/images/show/completed-elder-1920.jpg
	new file:   data/images/show/completed-park-people-1280.jpg
	new file:   data/images/show/completed-students-640.jpg
	new file:   data/images/show/dog-640.jpg
	new file:   data/images/show/models-hero.svg
	new file:   data/images/show/sayitYOLO.jpg
	new file:   data/images/show/segmentation_ex1.png
	new file:   data/images/show/segmentation_ex2.png
	new file:   data/images/show/ssd-head.png
	new file:   data/images/show/ssd_output.jpg
	new file:   data/images/show/woman-640_yolox.jpg
	new file:   data/images/show/yolo_multi_exmp.png
	new file:   data/images/test/bike-640.jpg
	new file:   data/images/test/elder-1920.jpg
	new file:   data/images/test/hanoi-640.jpg
	new file:   data/images/test/park-people-1280.jpg
	new file:   data/images/test/seg_example_01.png
	new file:   data/images/test/seg_example_02.jpg
	new file:   data/images/test/sport-1280.jpg
	new file:   data/images/test/sport-640.jpg
	new file:   data/images/test/students-640.jpg
	new file:   data/images/test/traffic-640.jpg
	new file:   data/images/test/twopeople_dog.jpg
	new file:   data/images/user-upload/2021-04-30T09-04-47-951135-1.png
	new file:   data/images/user-upload/2021-04-30T09-15-57-519880-10.jpeg
	new file:   data/images/user-upload/2021-04-30T09-43-21-456215-3.jpeg
	new file:   data/images/user-upload/2021-04-30T10-34-11-896590-5.jpeg
	new file:   data/yolo.h5
	new file:   docker-compose.yml
	new file:   e2c_warning.py
	new file:   enet_data/enet-cityscapes/enet-classes.txt
	new file:   enet_data/enet-cityscapes/enet-colors.txt
	new file:   enet_data/enet-cityscapes/enet-model.net
	new file:   enet_data/images/example_02.jpg
	new file:   enet_data/images/example_03.jpg
	new file:   enet_data/images/example_04.png
	new file:   enet_data/images/test2.jpg
	new file:   enet_data/images/test3.jpg
	new file:   enet_data/images/test4.jpg
	new file:   enet_data/images/test5.jpg
	new file:   enet_data/images/test6.jpg
	new file:   enet_data/images/test_image.jpg
	new file:   fake.py
	modified:   image_func.py
	new file:   requirements.txt
	new file:   saveCap.py
	new file:   scaledown.py
	new file:   semanticSeg.py
	modified:   tensorflow_od.py
	new file:   video_func.py
	new file:   yolo.py
	new file:   yolo_model/darknet53.py
	new file:   yolo_model/yolo_model.py

```

뉴 파일들로 추가가 되어 있는 상태.. 즉 add를 한 상태이기 때문에 
다시 add된 것을 취소 시켜줘야한다 

이거는 다시 git restore --stage <file> 으로 하면 되는데

git restore --staged data/
이런식으로 하면 해당 디렉토리가 다 취소됨

그리고 * 로 했더니 에러 발생.;;
그래서 일일이 하나씩 해줌 
화살표 위에 키랑 탭을 이용해서 하면 뭐.. 금방 한다

마지막으로 하면 git st
라고 해보면

```
git st
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   .gitignore
	modified:   app.py
	modified:   image_func.py
	modified:   tensorflow_od.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Dockerfile
	data/
	docker-compose.yml
	e2c_warning.py
	fake.py
	requirements.txt
	saveCap.py
	scaledown.py
	semanticSeg.py
	video_func.py
	yolo.py
```

다시 마지막 add 로 staged영역에 들어가기 전의 상태로 되돌린다
위의 파일들처럼 추적하고 있는 파일들과 추적안하고 있는 상태의 파일들로 돌리는 것임

이제 다시 이그노어 리스트를 다시 정리하고 
다시 제대로 add 
커밋전에 data 의 용량이 큰것들이 잘 빠져있는지 확인 후 
다시 커밋 푸쉬하면 되겠다

