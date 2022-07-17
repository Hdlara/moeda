FROM node:14.15.1 as build-step

RUN mkdir -p /app

WORKDIR /app

COPY package.json /app/package.json

RUN npm install
