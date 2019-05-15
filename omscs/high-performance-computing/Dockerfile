FROM ubuntu:trusty

RUN apt-get update \
    && apt-get -y install software-properties-common \
    && apt-add-repository -y ppa:git-core/ppa \
    && apt-get update \
    && apt-get -y install \
        build-essential \
        zip \
        unzip \
        libgmp-dev \
        gcc-multilib \
        valgrind \
        openmpi-bin \
        openmpi-doc \
        libopenmpi-dev \
        python-pip \
        python-dev \
        python-numpy \
        python-scipy \
        python-matplotlib \
        git \
        libffi6 \
        libffi-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

RUN pip install \
    ndg-httpsclient \
    pyasn1 \
    requests \
    future \
    numpy \
    pandas \
    pyopenssl

ENV SHELL /bin/bash
WORKDIR /omscs
