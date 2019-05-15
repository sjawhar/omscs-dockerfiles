FROM debian:sid-slim

# Install brave-browser
RUN apt-get update \
 && apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        fonts-symbola \
        gnupg \
        hicolor-icon-theme \
        libcanberra-gtk* \
        libgl1-mesa-dri \
        libgl1-mesa-glx \
        libpango1.0-0 \
        libpulse0 \
        libv4l-0 \
        --no-install-recommends \
 && curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add - \
 && echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ bionic main" >> /etc/apt/sources.list.d/brave-browser-release-bionic.list \
 && apt-get update \
 && apt-get install -y \
        brave-browser \
        brave-keyring \
 && rm -rf /var/lib/apt/lists/* \
 && apt-get purge -y --auto-remove curl

# Add brave-browser user
RUN groupadd -g 1000 brave-browser \
 && useradd -u 1000 -g brave-browser -G audio,video brave-browser \
 && mkdir -p /home/brave-browser/Downloads \
 && chown -R brave-browser:brave-browser /home/brave-browser

# Run as non privileged user
USER brave-browser

ENTRYPOINT ["/usr/bin/brave-browser"]
CMD ["--user-data-dir=/data"]