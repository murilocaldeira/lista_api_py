FROM python:3.7-alpine

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /statsapi

COPY ./app.py /app.py
COPY ./statsapi/data_store.py /statsapi/data_store.py
COPY ./statsapi/operation.py /statsapi/operation.py

EXPOSE 5000

CMD ["python", "app.py"]
