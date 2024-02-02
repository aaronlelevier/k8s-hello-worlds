#!/bin/bash

app="hello"

docker build -t ${app} .

docker run -d -p 5001:5000 \
  --name=${app} \
  -v $PWD:/app ${app}
