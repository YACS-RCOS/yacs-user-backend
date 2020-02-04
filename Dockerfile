FROM python:3.7 
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
COPY config.py.example config.py

CMD [ "python", "app.py" ]
