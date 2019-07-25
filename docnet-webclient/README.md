# Angular web client

## Get the template code

```
git clone --depth=1 https://github.com/angular/angular-seed.git docnet-webclient
cd docnet-webclient
```

## Run by node.js

```
npm install
npm install express --save
vim app.js
	var express = require("express");
    var app = express();
    var router = express.Router();

    var path = __dirname + '/app/';
    const PORT = 8002;
    const HOST = 0.0.0.0;

    router.use(function (req,res,next) {
        console.log("/" + req.method);
        next();
    });

    router.get("/",function(req,res){
        res.sendFile(path + "index.html");
    });

    app.use(express.static(path));
    app.use("/", router);

    app.listen(8002, function () {
        console.log('Web app listening on port '+PORT+'!')  
    })
node app.js
```

http://localhost:8002

## Run by Docker 

Make sure you did the configuration on the previous section  

```
# The app, inside container, will run on 8002 port, and 
# the container, inside host, will run on 8002 port
vim Dockerfile
	FROM node:10
	RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app	
	WORKDIR /home/node/app	
	COPY package*.json ./	
	RUN npm install	
	COPY . .	
	COPY --chown=node:node . .	
	USER node	
	EXPOSE 8002	
	CMD [ "node", "app.js" ]	
	vim .dockerignore
	node_modules
	npm-debug.log
	Dockerfile
	.dockerignore
docker build -t docnet-webclient-image .
docker run --name docnet-webclient -p 8002:8002 -d docnet-webclient-image
```

http://localhost:8002

## Run by Docker Compose

Make sure you did the configuration on the previous section

```
vim docker-compose.yml
	# This file is used run/config services inside the docker container
	# (such as a postgres configuration or run a web application)
	
	version: '3.3'
	
	services:
	  web:
	    build: .
	    container_name: docnet-webclient
	    command: node app.js
	    ports:
	      - "8002:8002" # HOST_PORT:CONTAINER_PORT

docker-compose up -d
```

http://localhost:8002
