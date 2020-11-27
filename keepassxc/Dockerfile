FROM debian:bullseye-slim
RUN apt-get update \
 && apt-get install -y \
      keepassxc=2.6.2+dfsg.1-1 \
 && rm -rf /var/lib/apt/lists/*

RUN groupadd -g 1000 keepassxc \
 && useradd -m -u 1000 -g keepassxc keepassxc

USER keepassxc
ENTRYPOINT ["keepassxc"]
