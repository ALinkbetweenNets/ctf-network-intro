FROM debian:stable-slim


ARG CHAL2_FLAG=flag{grossssssssss3r_ha1_dim_dim}


RUN DEBIAN_FRONTEND=noninteractive apt update -y && DEBIAN_FRONTEND=noninteractive apt upgrade -y && DEBIAN_FRONTEND=noninteractive apt install vim python-is-python3 socat iproute2 -y python3-pip python3-venv

WORKDIR /opt

COPY ./requirements.txt /opt/
RUN python -m venv .venv
RUN source .venv/bin/activate
RUN pip3 install -r requirements.txt

COPY ./server.py /opt/
COPY ./templates /opt/templates
COPY ./static /opt/static

RUN sed -i s/FLAG_PLACEHOLDER/$CHAL2_FLAG/g /opt/templates/flag.html

CMD /usr/local/bin/gunicorn -w 4 -b 0.0.0.0:80 server:app
