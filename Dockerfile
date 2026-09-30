FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY app.py /app/app.py

RUN mkdir -p /data

EXPOSE 8080

CMD ["python", "app.py"]
