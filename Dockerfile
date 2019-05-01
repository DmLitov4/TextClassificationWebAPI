FROM python:3

ENV DODOENV 1
RUN mkdir /dodo
WORKDIR /dodo
COPY . /dodo/
RUN pip install -r requirements.txt