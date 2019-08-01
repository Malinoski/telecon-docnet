FROM node:10

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY package*.json ./

RUN npm install
RUN npm install express --save

COPY . .

COPY --chown=node:node . .

USER node

EXPOSE 8002

# CMD [ "node", "app.js" ]
