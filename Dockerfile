#Docker File -django
FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV http_proxy=http://10.1.2.20:8080
ENV https_proxy=http://10.1.2.20:8080
ENV no_proxy=localhost
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install -r requirements.txt
COPY . /code/
