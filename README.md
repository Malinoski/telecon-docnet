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

http://localhost:8001/hello

## Deploy the web client

```
cd ..
cd docnet-webclient
docker-compose up -d
```

http://localhost:8002

