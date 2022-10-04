FROM python:3.10-slim-buster
MAINTAINER Roman Kojnok <roman.kojnok@protonmail.com>
ADD . /qafinalproject
WORKDIR /qafinalproject
RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "./run.py" ]
