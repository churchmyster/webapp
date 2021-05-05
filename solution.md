# WebApp

## Explanation
Web App is built as a python package. Allows client to interface with the server resource "Items".
## Features
* WebApp is served locally in port 3000.
* API allows clients to retrieve the current items, set the list of items, and delete all of the items.
* API endpoint accepts payloads in JSON format.
* Items object persists in memory.
* WebApp is containerized via Dockerfile.
 
## Future
* sqlalchemy can be utilized to database the items resource.


## How to use/build
Docker image can be build with the following command
```sh
sudo docker build -t dockerapp .
```

Image can run with the folloing command.
```sh
sudo docker run -p 3000:3000 dockerapp
```