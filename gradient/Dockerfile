FROM python:3-alpine
RUN apk add --no-cache --virtual build-dependencies \
        gcc \
        libffi-dev \
        musl-dev \
        openssl-dev \
        python3-dev \
 && pip3 install --no-cache-dir \
        gradient==0.7.0 \
 && apk del build-dependencies

RUN adduser -D gradient
WORKDIR /gradient
USER gradient
ENTRYPOINT ["gradient"]
CMD ["help"]
