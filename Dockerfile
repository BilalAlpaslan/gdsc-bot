FROM python:3.10

ADD requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install -U git+https://github.com/Rapptz/discord.py

ADD . .
CMD python ./main.py
