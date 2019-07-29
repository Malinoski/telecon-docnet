# Install using Docker 

## Get the code
```
git clone https://github.com/Malinoski/telecon-docnet telecon-docnet
cd telecon-docnet
```

## Deploy the web server 

```
cd docnet-webserver
docker-compose up -d 
```

http://localhost:8001 (username=admin, password=admin)

## Deploy the web client

```
cd ..
cd docnet-webclient
docker-compose up -d
```

http://localhost:8002

## Utils

* Destroy containers and images

```
docker stop docnet-webserver; docker rm docnet-webserver; docker rmi docnet-webserver_web
docker stop docnet-webclient; docker rm docnet-webclient; docker rmi docnet-webclient_web
```
