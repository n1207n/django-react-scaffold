FROM node:14.15-alpine

RUN apk add --no-cache bash

WORKDIR /code

# add `/app/node_modules/.bin` to $PATH
ENV PATH /code/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts -g --silent

# add app
COPY . ./

EXPOSE 3000

CMD ["npm", "start"]
