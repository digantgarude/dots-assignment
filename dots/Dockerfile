# Select python image v3
FROM python:3

# Setting workdir to app inside docker
WORKDIR /app

# First copy all files inside docker container
COPY . .

# Install all requirements
RUN pip install -r requirements.txt

# Run migrations and start server
CMD python3 manage.py makemigrations; python3 manage.py migrate; python3 manage.py runserver 0.0.0.0:8000

EXPOSE 8000