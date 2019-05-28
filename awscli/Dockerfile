FROM alpine:3.9
RUN apk add --no-cache \
        docker=18.09.1-r0 \
        groff=1.22.3-r2 \
        python3=3.6.8-r2
RUN apk add --no-cache --virtual build-dependencies \
        gcc \
        musl-dev \
        py3-pip \
        python3-dev \
 && pip3 install --no-cache-dir \
        aws-sam-cli==0.16.0 \
        awscli==1.16.160 \
 && apk del build-dependencies

RUN adduser -D aws

WORKDIR /aws
USER aws
ENTRYPOINT ["aws"]
CMD ["help"]
