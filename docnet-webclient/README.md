# Angular web client

## TODO

* [feature] Create an service to logout, where can be used by all apps

* [feature] Create a service where can check all http response and alert adequally (a pattern to all). Ex.: If response.status==401, then, "Unauthorized"

* [tests] Create unit tests, like the samples located in e2e-testes folder

* [functionality] When open a create modals, this must cleared

* [feature] On first loads/login, the available urls must be collected (i.ex.: "http://localhost:8001/networks/", "http://localhost:8001/addresses/")

* [code updgrade] $scope.checkToken must be a service available to all apps

* [feature] Create generic services (to be used for any app) to delete and list, including only the url

* [code updgrade] Include all Javascript and CSS in package.json (for npm intall). There are some not included there, like bootstrap and bootbox 

* [feature] The restriction of create networks with the same name must be implement in the server side, not only in the client.


## Development

* Run a simple Angular in node.js

```
git clone --depth=1 https://github.com/angular/angular-seed.git docnet-webclient
cd docnet-webclient
npm install
npm install express --save
node app.js
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
