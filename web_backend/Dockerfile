FROM python:3.9.1-alpine3.12 as base

ENV WAITFORIT_VERSION="v2.4.1"

# For Pillow library
ENV LIBRARY_PATH=/lib:/usr/lib

RUN apk update
RUN apk add --no-cache --virtual .fetch-deps \
    ca-certificates \
    openssl \
    tar

RUN apk add --upgrade --no-cache "postgresql-client" "postgresql-contrib" "postgresql-dev" \
    bash curl py-pip g++ \
    linux-headers gcc make \
    libffi-dev wget jpeg-dev zlib-dev \
    graphviz graphviz-dev ttf-freefont \
    libxml2-dev xmlsec-dev libxslt-dev \
    # Add Rust compiler for cryptography pypi
    rust cargo musl-dev

RUN curl -o /usr/local/bin/waitforit -sSL https://github.com/maxcnunes/waitforit/releases/download/$WAITFORIT_VERSION/waitforit-linux_amd64 && \
    chmod +x /usr/local/bin/waitforit

ADD myapp/requirements/ /tmp
RUN pip install --upgrade pip
RUN pip install -r /tmp/base.txt

ADD . /code/

RUN mkdir -p /data/static
RUN mkdir -p /data/uploads

VOLUME /data

EXPOSE 8000

WORKDIR /code/

FROM base as dev
ENV RQFILE=dev.txt
RUN if [ -f /tmp/$RQFILE ]; then pip install -r /tmp/$RQFILE; else pip install -r /tmp/base.txt; fi

FROM base as prod
ENV RQFILE=prod.txt
RUN if [ -f /tmp/$RQFILE ]; then pip install -r /tmp/$RQFILE; else pip install -r /tmp/base.txt; fi
