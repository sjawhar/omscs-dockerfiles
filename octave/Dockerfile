FROM debian:buster as packages
RUN apt-get update \
 && apt-get install -y \
        autoconf \
        automake \
        bison \
        epstool \
        fig2dev \
        flex \
        g++ \
        gcc \
        gfortran \
        git \
        gnuplot \
        gperf \
        gzip \
        icoutils \
        libarpack2-dev \
        libblas-dev \
        libcurl4-gnutls-dev \
        libfftw3-dev \
        libfltk1.3-dev \
        libfontconfig1-dev \
        libfreetype6-dev \
        libgl1-mesa-dev \
        libgl2ps-dev \
        libglpk-dev \
        libgraphicsmagick++1-dev \
        libhdf5-dev \
        libjack-jackd2-dev \
        liblapack-dev \
        libosmesa6-dev \
        libpcre3-dev \
        libqhull-dev \
        libqrupdate-dev \
        libqscintilla2-qt5-dev \
        libqt5core5a \
        libreadline-dev \
        librsvg2-bin \
        libsndfile1-dev \
        libsuitesparse-dev \
        libsundials-dev \
        libtool \
        libxft-dev \
        llvm-dev \
        make \
        openjdk-11-jdk \
        perl \
        portaudio19-dev \
        pstoedit \
        qtbase5-dev \
        qttools5-dev \
        qttools5-dev-tools \
        rsync \
        tar \
        texinfo \
        texlive \
        texlive-latex-extra \
        wget \
        zlib1g-dev

WORKDIR /source
RUN wget https://ftp.gnu.org/gnu/octave/octave-6.1.0.tar.gz \
 && tar -xzf octave-6.1.0.tar.gz

ARG OCTAVE_DIR=/opt/octave
WORKDIR /source/octave-6.1.0
RUN mkdir .build \
 && cd .build \
 && ./../configure --prefix=${OCTAVE_DIR} \
 && make -j2 \
 && make check \
 && make install


FROM debian:buster-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    libamd2 \
    libarpack2 \
    libasound2 \
    libblas3 \
    libbz2-1.0 \
    libc6 \
    libcamd2 \
    libccolamd2 \
    libcholmod3 \
    libcolamd2 \
    libcxsparse3 \
    libfftw3-double3 \
    libfftw3-single3 \
    libfltk-gl1.3 \
    libfltk1.3 \
    libfreetype6 \
    libgcc1 \
    libgl1 \
    libglpk40 \
    libglu1-mesa \
    libgomp1 \
    libklu1 \
    liblapack3 \
    liboctave6 \
    libopenblas-base \
    libportaudio2 \
    libqhull7 \
    libqrupdate1 \
    libqscintilla2-qt5-13 \
    libqt5core5a \
    libqt5gui5 \
    libqt5help5 \
    libqt5network5 \
    libqt5opengl5 \
    libqt5printsupport5 \
    libqt5sql5 \
    libqt5widgets5 \
    libsndfile1 \
    libstdc++6 \
    libsuitesparseconfig5 \
    libumfpack5 \
    libx11-6 \
    octave-common \
    texinfo \
    zlib1g

ARG APP_USER=octave
ARG UID=1000
ARG GID=1000
RUN addgroup --gid ${GID} ${APP_USER} \
 && adduser \
    --disabled-password \
    --gecos ${APP_USER} \
    --gid ${GID} \
    --uid ${UID} \
    ${APP_USER}

ARG OCTAVE_DIR=/opt/octave
COPY --from=packages ${OCTAVE_DIR} ${OCTAVE_DIR}
ENV PATH=${PATH}:${OCTAVE_DIR}/bin
ENV OCTAVE_DIR=${OCTAVE_DIR}

WORKDIR /home/${APP_USER}
USER ${APP_USER}
ENTRYPOINT ["octave"]
