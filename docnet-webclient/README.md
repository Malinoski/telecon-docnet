# Angular web client

## Development

* Get an Angular template code

```
git clone --depth=1 https://github.com/angular/angular-seed.git docnet-webclient
```

* Run using node.js

```
cd docnet-webclient
npm install
npm install express --save
node app.js
```

* Test 

http://localhost:8002

## Deploy 

* From Docker run

```
docker build -t docnet-webclient-image .
docker run --name docnet-webclient -p 8002:8002 -d docnet-webclient-image
```

* From Docker Compose

```
docker-compose up -d
```

* Test

http://localhost:8002

## Utils

* Destroy containers and image

```
docker stop docnet-webclient; docker rm docnet-webclient; docker rmi docnet-webclient_web
```
