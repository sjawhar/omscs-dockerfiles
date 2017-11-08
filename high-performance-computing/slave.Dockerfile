FROM sjawhar/omscs-hpc

RUN apt-get update \
 && apt-get install -y openssh-server \
 && rm -rf /var/apt/lists/*

ENV NOTVISIBLE "in users profile"
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd \
 && echo "export VISIBLE=now" >> /etc/profile \
 && mkdir -p /var/run/sshd

RUN ln -s /omscs /usr/local/bin/omscs
