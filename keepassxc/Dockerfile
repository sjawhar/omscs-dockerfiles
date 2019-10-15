FROM debian:bullseye-slim
RUN apt-get update \
 && apt-get install -y \
      keepassxc \
 && rm -rf /var/lib/apt/lists/*

RUN groupadd -g 1000 keepassxc \
 && useradd -u 1000 -g keepassxc keepassxc

USER keepassxc
ENTRYPOINT ["keepassxc"]
