FROM python:3.10


WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src/ .
ENV PYTHONPATH=src
CMD python app.py
