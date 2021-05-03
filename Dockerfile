FROM python:alpine

ARG version

COPY ./dist/docker_sqs_consumer-${version}-py3-none-any.whl . 

RUN pip install docker_sqs_consumer-${version}-py3-none-any.whl

CMD ["consume"]
