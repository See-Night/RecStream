FROM node:latest

LABEL description="RecStream's Document"

WORKDIR /docs

RUN npm install -g docsify-cli@latest

EXPOSE 3000/tcp

ENTRYPOINT docsify serve .
