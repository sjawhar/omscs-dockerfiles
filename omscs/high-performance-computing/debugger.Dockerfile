FROM sjawhar/omscs-hpc

RUN apt-get update \
  && apt-get install -y curl apt-transport-https g++ gdb make \
  && curl https://download.sublimetext.com/sublimehq-pub.gpg | apt-key add - \
  && echo "deb https://download.sublimetext.com/ apt/stable/" | tee /etc/apt/sources.list.d/sublime-text.list \
  && apt-get update \
  && apt-get install sublime-text \
  && mkdir -p /root/.config/sublime-text-3/Installed\ Packages \
  && curl -o /root/.config/sublime-text-3/Installed\ Packages/Package\ Control.sublime-package https://packagecontrol.io/Package%20Control.sublime-package \
  && rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8

WORKDIR /root/omscs
