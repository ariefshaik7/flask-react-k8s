FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/backend/

EXPOSE 5001

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "backend.app:create_app()"]