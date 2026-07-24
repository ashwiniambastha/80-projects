FROM python:3.11-slim 

WORKDIR /app
COPY . /app
RUN pip install -r requirements.tx
CMD ["python", "flask_api/main.py"]