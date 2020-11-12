FROM circleci/circleci-cli:0.1.10583-alpine

RUN addgroup -g 1000 circleci \
  && adduser -u 1000 -G circleci -s /bin/sh -D circleci
USER circleci
