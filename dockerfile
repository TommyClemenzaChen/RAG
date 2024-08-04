FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]