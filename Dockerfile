FROM python:3.9

WORKDIR /app

COPY . /app

# Copy images to the static folder
COPY images /app/static

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

