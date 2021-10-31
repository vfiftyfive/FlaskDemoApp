#!/bin/bash

docker rmi vfiftyfive/flask_ascii -f
docker buildx build --platform linux/amd64,linux/arm64 --push -t vfiftyfive/flask_ascii .
docker run -p 80:80 vfiftyfive/flask_ascii

