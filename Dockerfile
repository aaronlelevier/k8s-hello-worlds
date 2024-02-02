FROM python:3.11-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY garden.py /app/garden.py

RUN pip install -r requirements.txt

CMD [ "python", "garden.py" ]

# TODO: is this needed?
EXPOSE 5000
