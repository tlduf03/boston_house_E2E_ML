#pull the base image from dockerhub
FROM python:3.7

#copy current location to /app folder with in that base image
COPY . /app

#same location
WORKDIR /app

RUN pip install -r requirements.txt

#port
EXPOSE $PORT

#helps us to run the app on heroku
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
