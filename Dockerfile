FROM python:3.11-buster
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
RUN apt-get update -y
COPY . .
CMD ['daphne', 'chat_city.asgi:application']
