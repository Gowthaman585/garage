FROM rockylinux/rockylinux:9
RUN dnf install -y openssh-server && ssh-keygen -A
RUN echo 'root:ansiblepassword' | chpasswd && echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
