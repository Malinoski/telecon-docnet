# Angular web client

## TODO

* [feature] Create an service to logout, where can be used by all apps

* [feature] Create a service where can check all http response and alert adequally (a pattern to all). Ex.: If response.status==401, then, "Unauthorized"

* [tests] Create unit tests, like the samples located in e2e-testes folder

* [Design] Create a principal header on top of page

## Development

* Run a simple Angular in node.js

```
git clone --depth=1 https://github.com/angular/angular-seed.git docnet-webclient
cd docnet-webclient
npm install
npm install express --save
node app.js # here are configured the http port used
```

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
