FROM debian:stable-slim


ARG CHAL0_FLAG=flag{kl3in3r_ha1_dim_dim}


RUN DEBIAN_FRONTEND=noninteractive apt update -y && DEBIAN_FRONTEND=noninteractive apt upgrade -y && DEBIAN_FRONTEND=noninteractive apt install vim python-is-python3 socat iproute2 -y

WORKDIR /opt

COPY ./vuln.py /opt/
COPY ./start.sh /opt/
RUN chmod +x /opt/start.sh

RUN sed -i s/FLAG_PLACEHOLDER/$CHAL0_FLAG/g /opt/vuln.py

ENTRYPOINT ["./start.sh" ]
