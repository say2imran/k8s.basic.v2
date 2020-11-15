#!/bin/bash

for folder in frontend getter putter
do
  echo "Starting to docker build"
  echo $folder
  cd $folder
  docker build -t "${folder}_image" .
  cd ..
  echo "Done with building docker build"
done

echo "Running container"
docker ps
echo "Stopping containers"
docker stop  $(docker ps -a -q)
docker rm  $(docker ps -a -q)

docker network create getter_putter_network

echo "Restarting containers"
docker run -d -p 8080:8080 --name frontend_container --network getter_putter_network frontend_image
docker run -d -p 8081:8081 --name getter_container --network getter_putter_network getter_image
docker run -d -p 8082:8082 --name putter_container --network getter_putter_network putter_image

docker container ls