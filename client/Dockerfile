FROM node:23 AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
FROM httpd:2.4 AS production-stage
COPY --from=build-stage /app/build/ /usr/local/apache2/htdocs/
EXPOSE 80