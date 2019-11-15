FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
# CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]