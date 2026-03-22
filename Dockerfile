FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install PyYAML
COPY . .
CMD ["python", "main.py"]