FROM node:alpine
WORKDIR /usr/src/app
COPY package*.json /usr/src/app/
RUN npm install
EXPOSE 5001
COPY . /usr/src/app/
CMD ["node","index.js"]