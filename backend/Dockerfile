FROM --platform=linux/amd64 python:3.10-slim-buster as build
WORKDIR /backend
COPY requirements.txt /backend
RUN pip install -r requirements.txt
COPY . /backend
EXPOSE 5000
# CMD ("python" "main.py")