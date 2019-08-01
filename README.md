# Install 

### Get the code
```
git clone https://github.com/Malinoski/telecon-docnet telecon-docnet
cd telecon-docnet
```

### Deploy the web server 

```
cd docnet-webserver
docker-compose up -d 
```

http://localhost:8001

### Deploy the web client

```
cd ..
cd docnet-webclient
docker-compose up -d
```

Available users (```$USERNAME:$PASSORD```): 

```admin:admin``` and ```user01:user01```

http://localhost:8002 


# Uninstall

```
docker stop docnet-webserver; docker rm docnet-webserver; docker rmi docnet-webserver_web
docker stop docnet-webclient; docker rm docnet-webclient; docker rmi docnet-webclient_web
```
