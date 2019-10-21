FROM debian:bullseye-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        bluez \
        libcap2-bin \
        python3 \
        python3-pyqt5 \
        python3-pyqt5.qtopengl \
 && rm -rf /var/lib/apt/lists/* \
 && setcap 'cap_net_raw,cap_net_admin+eip' `which hcitool` \
 && echo '#!/bin/sh' > /usr/local/bin/sudo \
 && echo 'echo $@' >> /usr/local/bin/sudo \
 && chmod +x /usr/local/bin/sudo

RUN DEV_PACKAGES="\
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
 && apt-get remove -y $DEV_PACKAGES \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/* \
 && rm -r /root/.cache

RUN groupadd -g 1000 muselsl \
 && useradd -m -u 1000 -g muselsl muselsl

WORKDIR /home/muselsl
USER muselsl
ENTRYPOINT ["muselsl"]
