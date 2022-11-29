#Docker File
FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV http_proxy=http://10.1.2.20:8080
ENV https_proxy=http://10.1.2.20:8080
ENV no_proxy=localhost,*.impuestos.gob.bo,webmail.impuestos.gob.bo,dev.impuestos.gob.bo,repo.impuestos.gob.bo,172.19.1.128,192.168.150.136,192.168.150.13
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install -r requirements.txt
COPY . /code/
