FROM python:2.7.13
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /codigo
 WORKDIR /codigo
 ADD requirements.txt /codigo/
 RUN pip install -r requirements.txt
 ADD . /codigo/
