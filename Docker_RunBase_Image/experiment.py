FROM ubuntu
WORKDIR /tem # working directory inside the container
RUN echo "Learning the docker"
ENV     myname=ankit   #key=value
COPY     experiment.py /tmp           #--chown=user:group#source dest
ADD test /tmp                 # test file will add to the your tmp folder of baseimage





D:\study\Docker_RunBase_Image>docker run --name latestcontainer -it newimage /bin/sh
# ls
test.tar.gz  testfile
#

# echo $myname
ankit
#