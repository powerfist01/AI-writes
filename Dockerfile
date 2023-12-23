FROM python:3.9.18-slim-bullseye

ENV APP_HOME /app

WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --allow-unauthenticated vim

COPY requirements.txt $APP_HOME

RUN pip install --upgrade pip
RUN pip3 install --root-user-action=ignore -r requirements.txt

CMD ["gunicorn", "--reload", "-w", "4", "-b", "0.0.0.0:5000", "manage:app"]
