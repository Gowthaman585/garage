FROM ubuntu:latest
RUN apt-get update && apt-get install -y openssh-server 
RUN echo 'root:ansiblepassword' | chpasswd && echo 'PermitRootLogin yes' >> etc/ssh/sshd_config
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]

