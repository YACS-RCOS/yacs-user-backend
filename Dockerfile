FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]