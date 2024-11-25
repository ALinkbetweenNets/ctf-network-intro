FROM debian:stable-slim



RUN DEBIAN_FRONTEND=noninteractive apt update -y && DEBIAN_FRONTEND=noninteractive apt upgrade -y && DEBIAN_FRONTEND=noninteractive apt install vim python-is-python3 socat iproute2 -y python3-flask gunicorn3

WORKDIR /opt

COPY ./requirements.txt /opt/

COPY ./server.py /opt/
COPY ./templates /opt/templates
COPY ./static /opt/static

CMD /usr/bin/gunicorn -w 4 -b 0.0.0.0:80 server:app
