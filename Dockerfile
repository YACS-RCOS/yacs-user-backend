FROM python:3.7
WORKDIR /app

COPY . /app
COPY config.py.example config.py

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
