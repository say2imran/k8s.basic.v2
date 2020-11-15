#!/bin/bash

read -p "Enter your docker repo name: " docker_repo

if [ -z "$docker_repo" ]
then
  echo "Docker repo cannot be empty"
  exit 0
fi

apps=(frontend getter putter)
image_version_pattern="_image:v2"

echo "=====================Here goes to build images==========================="

for folder in ${apps[@]}
do
  echo "Starting to docker build for " $folder
  cd $folder
  echo "This will be build"
  echo "RUNNING --> docker build -t \"$docker_repo/${folder}${image_version_pattern}\" ."
  docker build -t "$docker_repo/${folder}${image_version_pattern}" .
  cd ..
  echo "Done with building docker build"
done

echo "=====================Here goes to push to docker repo==========================="
docker login

for folder in ${apps[@]}
do
  echo "Pushing image:" "$docker_repo/${folder}${image_version_pattern}"
  docker push "$docker_repo/${folder}${image_version_pattern}"
done

echo "=====================Done with the build and push==========================="