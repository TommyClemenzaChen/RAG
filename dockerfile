FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN apt update -y

EXPOSE 8000

RUN pip install -r requirements.txt
CMD ["python3", "app.py"]