FROM nginx:latest

ARG CHAL0_FLAG=flag{baby_ha1_dum_dum}

COPY ./html /etc/nginx/html/
RUN sed -i s/FLAG_PLACEHOLDER/$CHAL0_FLAG/g /etc/nginx/html/flag.css