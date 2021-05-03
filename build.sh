#!/bin/bash

version=`poetry version --short`
poetry build
docker build . -t dfqalves/sqs:$version --build-arg version=$version

docker tag dfqalves/sqs:$version 760373735544.dkr.ecr.us-east-1.amazonaws.com/devxp/tesseract/queueconsumertest:$version
docker push 760373735544.dkr.ecr.us-east-1.amazonaws.com/devxp/tesseract/queueconsumertest:$version


