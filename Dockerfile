# this is an official Python runtime, used as the parent image
FROM python:alpine3.19

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN apk add --no-cache libpq-dev musl-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

# unblock port 80 for the Flask app to run on
EXPOSE 5000

# execute the Flask app
# CMD ["python", "app.py"] 
CMD ["flask", "run", "--host=0.0.0.0"]