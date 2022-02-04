FROM python:3.10-alpine

ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

ENV MODE="prod"

ADD . .
CMD python ./main.py
