FROM nginx:latest

ARG CHAL0_FLAG=flag{kl3in3r_ha1_dum_dum}

COPY ./html /etc/nginx/html/
RUN sed -i s/FLAG_PLACEHOLDER/$CHAL0_FLAG/g /etc/nginx/html/flag.css