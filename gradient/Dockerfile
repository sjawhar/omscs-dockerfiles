FROM python:3.8-alpine
RUN apk add --no-cache \
        libstdc++ \
        openblas \
 && apk add --no-cache --virtual build-dependencies \
        build-base \
        gcc \
        libffi-dev \
        musl-dev \
        openblas-dev \
        openssl-dev \
        python3-dev \
 && pip3 install --no-cache-dir \
        gradient==1.1.0 \
 && apk del build-dependencies

RUN adduser -D gradient
WORKDIR /gradient
USER gradient
ENTRYPOINT ["gradient"]
CMD ["help"]
