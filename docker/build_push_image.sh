#!/bin/bash
#
# Builds and pushes a new 'rterminal' multiarch docker image
# Image tag is specified by first argument
#

IMAGE_TAG=0

if [ "$1" = "" ]; then
  echo "Image tag should be specified as argument"
  exit 1
else
  IMAGE_TAG=$1
fi

if ! [ -f "./rterminal.dockerfile" ]; then
  echo "Docker file not found: ./rterminal.dockerfile"
  exit 1
fi

docker buildx build                     \
    --platform linux/amd64,linux/arm64  \
    -t giobyte8/rterminal:"$IMAGE_TAG"  \
    -f rterminal.dockerfile              \
    --push                              \
    ..

echo
echo "Verion $IMAGE_TAG of rterminal was released to docker registry"
