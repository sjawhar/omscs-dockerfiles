FROM debian:buster-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        bluez \
        libcap2-bin \
        python3 \
        python3-pyqt5 \
        python3-pyqt5.qtopengl \
        sudo \
 && rm -rf /var/lib/apt/lists/* \
 && FAKE_SYSTEMCTL="/usr/local/bin/systemctl" \
 && echo '#!/bin/sh' > $FAKE_SYSTEMCTL \
 && echo 'echo tried to call systemctl $@' >> $FAKE_SYSTEMCTL \
 && chmod +x $FAKE_SYSTEMCTL \
 && setcap 'cap_net_raw,cap_net_admin+eip' `which hcitool` \
 && echo "muselsl ALL=(ALL) NOPASSWD: `which hciconfig`, $FAKE_SYSTEMCTL" >> /etc/sudoers

RUN DEV_PACKAGES=" \
        build-essential \
        gfortran \
        libfreetype6-dev \
        libopenblas-dev \
        python3-dev \
        python3-pip \
    " \
 && apt-get update \
 && apt-get install -y $DEV_PACKAGES \
 && pip3 install --ignore-installed \
        Cython \
        mne \
        numpy \
        setuptools \
        six \
        vispy \
 && pip3 install \
        muselsl \
 && apt-get purge -y --auto-remove $DEV_PACKAGES \
 && rm -rf /var/lib/apt/lists/* \
 && rm -r /root/.cache

RUN groupadd -g 1000 muselsl \
 && useradd -m -u 1000 -g muselsl muselsl

WORKDIR /home/muselsl
USER muselsl
ENTRYPOINT ["muselsl"]
