FROM debian:buster
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        groff \
        less \
 && rm -rf /var/lib/apt/lists/*

COPY --from=amazon/aws-cli:2.0.56 /usr/local/aws-cli/v2/current /usr/local

RUN addgroup --gid 1000 aws \
 && adduser \
    --disabled-password \
    --gecos nte \
    --gid 1000 \
    --uid 1000 \
    aws

USER aws
ENTRYPOINT ["aws"]
CMD ["help"]
