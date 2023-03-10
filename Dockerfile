# Build: docker build -t node-web-app .
from node:10

workdir /usr/src/app
copy package*.json ./

run npm install

# Bundle app source

copy . .

expose 8080

cmd [ "node", "server" }

# Path: Dockerfile
