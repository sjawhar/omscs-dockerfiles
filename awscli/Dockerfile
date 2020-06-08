FROM alpine:3.12
RUN apk add --no-cache \
        docker=19.03.11-r0 \
        groff=1.22.4-r0 \
        py3-colorama=0.4.3-r0 \
        py3-requests=2.23.0-r0 \
        python3=3.8.3-r0
RUN apk add --no-cache --virtual build-dependencies \
        gcc \
        musl-dev \
        py3-pip \
        python3-dev \
 && pip3 install --no-cache-dir \
        aws-sam-cli==0.52.0 \
        awscli==1.18.73 \
 && apk del build-dependencies

RUN adduser -D aws

WORKDIR /aws
USER aws
ENTRYPOINT ["aws"]
CMD ["help"]
