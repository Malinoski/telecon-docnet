# Introduction


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

```user01:user01``` and ```user02:user02```

http://localhost:8002 


# Uninstall

```
docker stop docnet-webserver; docker rm docnet-webserver; docker rmi docnet-webserver_web
docker stop docnet-webclient; docker rm docnet-webclient; docker rmi docnet-webclient_web
```

# How to use

The following 8 steps illustrate how to create, edit, view and remove networks and address. 

_1. Access the web client at http://localhost:8001, and enter with the username ```user01``` and password ```user01```_
![alt text](./documentation-media/01.png)

_2. You will see an empty list of networks. Lets create on the button "Create Network"_
![alt text](./documentation-media/02.png)

_3. Set the desired values:_
![alt text](./documentation-media/03.png)

_4. Now you can edit or remove the network on the action icons_
![alt text](./documentation-media/04.png) 

_5. Click on the hyperlink to create a new address:_
![alt text](./documentation-media/06.png)

_6. Click on the button "Create Address":_
![alt text](./documentation-media/07.png)

_7. Set the desired values:_
![alt text](./documentation-media/08.png)

_8. Now you can edit or remove the address on the action icons_
![alt text](./documentation-media/09.png)
