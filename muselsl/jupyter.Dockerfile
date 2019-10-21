FROM jupyter/scipy-notebook:1386e2046833

USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        bluez \
        libcap2-bin \
 && rm -rf /var/lib/apt/lists/* \
 && setcap 'cap_net_raw,cap_net_admin+eip' `which hcitool`

USER jovyan
RUN conda install --yes \
    mne \
    pyqt \
    vispy \
 && conda clean -afy

RUN pip install --no-cache-dir \
    muselsl
