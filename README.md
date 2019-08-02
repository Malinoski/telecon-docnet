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

1. Access the web client at http://localhost:8001, and enter with the username ```user01``` and password ```user01```
![alt text](./documentation-media/01.png)

2. You will see an empty list of networks. Lets create on the button "Create Network"
![alt text](./documentation-media/02.png)

3. Set the desired values:
![alt text](./documentation-media/03.png)

4. Now you can edit or remove the network on the action icons
![alt text](./documentation-media/04.png) 

4. Click on the hyperlink to create a new address:
![alt text](./documentation-media/06.png)

5. Click on the button "Create Address":
![alt text](./documentation-media/07.png)

6. Set the desired values:
![alt text](./documentation-media/08.png)

7. Now you can edit or remove the address on the action icons
![alt text](./documentation-media/09.png)

8