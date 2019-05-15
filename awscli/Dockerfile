FROM alpine:3.9
RUN apk add --no-cache \
        docker=18.09.1-r0 \
        python3=3.6.8-r2
RUN apk add --no-cache --virtual build-dependencies \
        gcc \
        musl-dev \
        py3-pip \
        python3-dev \
 && pip3 install --no-cache-dir \
        awscli==1.16.143 \
        aws-sam-cli==0.15.0 \
 && apk del build-dependencies

RUN adduser -D aws

WORKDIR /aws
USER aws
ENTRYPOINT ["aws"]
CMD ["help"]
