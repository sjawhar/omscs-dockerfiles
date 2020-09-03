## Usage
### Bash Alias
```bash
pipenv () 
{ 
    local dirCache="${HOME}/.pipenv";
    local dirEnvs="${HOME}/.local/share/virtualenvs";
    mkdir -p "${dirCache}" "${dirEnvs}";
    local flagsShell='--user pipenv';
    local pipenvCmd="${@}";
    if [ "${1}" == "shell" ]; then
        flagsShell='--user root --entrypoint=';
        pipenvCmd='bash';
    fi;

    docker container run \
        $flagsShell \
        --rm -it \
        --log-driver none \
        --env PIP_NO_CACHE_DIR \
        --env PIPENV_INSTALL_TIMEOUT \
        --volume "$(pwd):$(pwd)" \
        --volume "${dirCache}:/home/pipenv/.cache" \
        --volume "${dirEnvs}:/home/pipenv/.local/share/virtualenvs" \
        --workdir "$(pwd)" \
        pipenv $pipenvCmd
}
```
* If ~/.pipenv and ~/.local/share/virtualenvs didn't exist before running for the first time, they will be owned by root and you'll run into permission issues. Make sure you take ownership of them (`chown -R`) on the host.
* Running `pipenv shell` opens a shell inside the container as root, which can be useful if you need to install other dev packages.

### Dockerfile
```dockerfile
FROM sjawhar/pipenv as packages
USER root
WORKDIR /scratch
COPY app/Pipfile app/Pipfile.lock ./
ARG PACKAGES_DIR=/scratch/packages
RUN PIP_PREFIX=${PACKAGES_DIR} \
    PIP_IGNORE_INSTALLED=1 \
    pipenv install --system --deploy --ignore-pipfile

FROM $PROD_IMAGE
ARG PACKAGES_DIR=/scratch/packages
COPY --from=packages ${PACKAGES_DIR} /usr/local
```