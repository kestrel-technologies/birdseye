FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY birdseye ./birdseye
COPY run.sh .
EXPOSE 8080
CMD ["./run.sh"]
