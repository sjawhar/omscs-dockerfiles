FROM ubuntu:14.04
RUN apt-get update \
 && apt-get install -y \
        build-essential \
        cmake \
        gfortran \
        git \
        libatlas-base-dev \
        libavcodec-dev \
        libavformat-dev \
        libffi-dev \
        libffi6 \
        libgtk2.0-dev \
        libjasper-dev \
        libjpeg8-dev \
        libpng12-dev \
        libswscale-dev \
        libtiff4-dev \
        libv4l-dev \
        pkg-config \
        python-dev \
        python-numpy \
        python-pip \
        python-scipy \
        software-properties-common \
        wget \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /source
RUN wget -O opencv-2.4.13.6.tar.gz https://github.com/opencv/opencv/archive/2.4.13.6.tar.gz \
 && tar -xzvf opencv-2.4.13.6.tar.gz \
 && mkdir opencv-2.4.13.6/build \
 && cd opencv-2.4.13.6/build \
 && cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_C_EXAMPLES=ON \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D WITH_GTK=ON \
        -D BUILD_EXAMPLES=ON \
        .. \
 && make \
 && make install \
 && ldconfig \
 && cd /source \
 && rm -rf opencv*

RUN pip install --upgrade \
        matplotlib==2.2.3 \
        mock==2.0.0 \
        nelson==0.4.3 \
        nose==1.3.7 \
        numpy==1.15.1 \
        scipy==0.18.1

RUN adduser --gecos 'CS 6476' --disabled-password pset
USER pset
WORKDIR /app
