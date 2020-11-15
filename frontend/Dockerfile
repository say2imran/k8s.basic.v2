FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "app_server:app", "--host", "0.0.0.0", "--port", "8080" ]