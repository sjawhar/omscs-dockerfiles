FROM python:3.7.9-slim-buster
RUN apt-get update \
 && apt-get install -y \
        build-essential \
 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir pipenv==2020.8.13
RUN groupadd -g 1000 pipenv \
 && useradd -m -u 1000 -g pipenv pipenv

WORKDIR /app
USER pipenv
ENTRYPOINT ["pipenv"]
CMD ["install"]
