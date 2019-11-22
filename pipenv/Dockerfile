FROM python:3.7-alpine
RUN pip install --no-cache-dir pipenv==2018.11.26
RUN addgroup -g 1000 pipenv \
  && adduser -u 1000 -G pipenv -s /bin/sh -D pipenv

WORKDIR /app
USER pipenv
ENTRYPOINT ["pipenv"]
CMD ["install"]
