FROM python:3.11-slim-bullseye

WORKDIR /flask-get-temp-data-accuweather

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "--app", "main.py", "run", "--host=0.0.0.0"]