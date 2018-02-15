FROM python:2.7.11

RUN pip install \
        future==0.16.0 \
        numpy==1.10.0 \
        pillow==3.1.1 \
        requests==2.18.4 \
        watchdog==0.8.3 \
        git+https://github.com/dpallot/simple-websocket-server.git

WORKDIR /agent
COPY serve.py index.html ./
ENTRYPOINT ["python", "serve.py"]
