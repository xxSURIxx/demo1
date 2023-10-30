FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install psutil

CMD ["python3","python_1.py"]
