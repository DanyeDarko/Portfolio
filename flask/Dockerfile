FROM python:3.5-stretch AS flask
WORKDIR /app
ADD . /app 
RUN python -m pip install -r requirements.txt

CMD ["uwsgi","app.ini"]
