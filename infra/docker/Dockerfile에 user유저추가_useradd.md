# user 만드는 것이랑 HOME 및 USER 지정
## HOME 지정은 env에서
## Create user "docker_noetic"
RUN useradd -m docker_melodic && \
    echo "docker_melodic:docker_melodic" | chpasswd && adduser docker_melodic sudo && \
    ## adduser {비번} sudo 임
    ## cp /root/.bashrc ${HOME} && \  ## bashrc 생기는 지 확인 필요
    ## mkdir ${HOME}/catkin_ws && \ ##docker-compose 에서 volumns연결시 만듬
    chown -R --from=root docker_melodic /home/docker_melodic

######
USER docker_melodic
WORKDIR ${HOME}/docker_melodic 
##WORKDIR에서 위치

