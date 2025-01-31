FROM python:3.9

WORKDIR /app

COPY . /app

# Ensure static assets are included in the build
RUN mkdir -p /app/static
COPY app/static /app/static

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

