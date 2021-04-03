# pull official base image
FROM node:14.15.1-alpine AS dev

# set working directory
WORKDIR /opt/project

ENV PATH /opt/project/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
RUN npm install --silent

# add app
COPY . ./

EXPOSE 3000

# start app
CMD ["npm", "run", "start"]

FROM dev AS build

RUN npm run build

# production environment
FROM nginx:stable-alpine AS prod
COPY --from=build /opt/project/build /usr/share/nginx/html

# nginx config for react router
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]