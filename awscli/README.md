AWS cli, containerized for your convenience.

# Usage
1. Build the image: `docker build -t awscli .`
2. Create a file in this directory called secrets.env, inserting the appropriate values.
    ```
    AWS_ACCESS_KEY_ID=<YOUR ACCESS KEY ID>
    AWS_SECRET_ACCESS_KEY=<YOUR SECRET ACCESS KEY>
    ```
3. Run `./aws.sh`
4. For even more awesome, create an alias: `alias aws=/path/to/aws-vpc/utils/awscli/aws.sh`
    - If you're not using Linux, use the `AWSCLI_DOCKER_BIN` and `AWSCLI_MOUNT_PATH` environment variables to make the command work for you. Docker for Windows example:
    ```bash
    AWSCLI_DOCKER_BIN="winpty docker" AWSCLI_MOUNT_PATH=//host_mnt/$(pwd) ./aws.sh
    ```


# Examples

## Create New VPN Client Config
```bash
aws ssm send-command --document-name ${DOCUMENT_NAME} \
    --parameters '{"clientname":["'${CLIENT_NAME}'"]}' \
    --instance-ids ${VPN_SERVER_INSTANCE_ID}
```

## Download VPN Client Config
```bash
aws s3 cp s3://threatspan-${STACK_NAME}-vpn-client-configs/client/${CLIENT_NAME}.zip ./${CLIENT_NAME}.zip
```
