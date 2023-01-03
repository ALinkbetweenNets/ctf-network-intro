FROM node:latest

WORKDIR /usr/app
COPY ./ /usr/app

RUN npm install

ENTRYPOINT [ "npm", "start", "--", "--host", "0.0.0.0", "--port", "80"]