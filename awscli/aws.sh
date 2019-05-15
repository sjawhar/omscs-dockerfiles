#!/bin/sh
AWSCLI_DOCKER_BIN="${AWSCLI_DOCKER_BIN:-docker}"
if [ -z "${AWSCLI_MOUNT_PATH}" ]; then
  AWSCLI_MOUNT_PATH=$(pwd)
fi
secrets_file=$(dirname "${0}")/secrets.env

${AWSCLI_DOCKER_BIN} run --rm -it ${AWSCLI_DOCKER_ARGS} \
  --env-file ${secrets_file} -e AWS_DEFAULT_REGION=eu-central-1 \
  -v "${AWSCLI_MOUNT_PATH}:/aws" awscli $@
