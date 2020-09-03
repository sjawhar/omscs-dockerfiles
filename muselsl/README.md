## Usage
### Bash Alias
```bash
muselsl()
{
    local DOCKER_XAUTH=/tmp/.docker.xauth
    local DOCKER_XSOCK=/tmp/.X11-unix

    docker run -it \
        --env DISPLAY \
        --env "XAUTHORITY=${DOCKER_XAUTH}" \
        --name muselsl \
        --net host \
        --privileged \
        --volume "$(pwd):/app" \
        --workdir /app \
        --volume "${DOCKER_XAUTH}:${DOCKER_XAUTH}" \
        --volume "${DOCKER_XSOCK}:${DOCKER_XSOCK}" \
        --volume "${HOME}/.config/muselsl/bluetooth:/etc/bluetooth" \
        --volume "${HOME}/.config/muselsl/dbus:/etc/dbus-1" \
        --volume "${HOME}/.config/muselsl/devices:/var/lib/bluetooth" \
        sjawhar/muselsl $@
}

```
* Make sure to generate `/tmp.docker.xauth` before running this command, as outlined in [this tutorial](http://wiki.ros.org/docker/Tutorials/GUI#The_isolated_way). This is only needed if you need to open the visualizations, or if you build an app on top of this container which needs to interact with the X11 socket. Alternatively, consider using [x11docker](https://github.com/mviereck/x11docker).
* If ~/.config/muselsl didn't exist before running for the first time, it will be owned by root and you'll run into permission issues. Make sure you take ownership of them (`chown -R`) on the host.

### Dockerfile
You can also use this image to build apps which depend on muse-lsl. Simply use `FROM sjawhar/muselsl` then install all the other system and pip packages you need.