# Tesseract Docker Image

This repository contains a Dockerfile to build and push a Tesseract OCR Docker image as an ML Runtime. 

## Build the Image

```sh
docker build -t dockerhub_username/tesseract:v1 . --no-cache
```

## Push to Docker Hub

```sh
docker push dockerhub_username/tesseract:v1
```

Replace `dockerhub_username` with your actual Docker Hub username.