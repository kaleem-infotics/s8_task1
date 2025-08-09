# app/Dockerfile

From python:3.9

WORKDIR /app

copy . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
