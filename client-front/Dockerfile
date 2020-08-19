FROM node:12

ENV TZ America/Lima

WORKDIR /app

COPY . .

RUN yarn install
RUN yarn global add @quasar/cli
RUN yarn build

EXPOSE 80
CMD ["yarn", "start"]