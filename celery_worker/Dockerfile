FROM python:3.9.18-slim-bullseye

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/

ENV C_FORCE_ROOT true

COPY . /queue
WORKDIR /queue

RUN pip install -U setuptools pip
RUN pip install -r requirements.txt

# hot code reloading
CMD watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- celery -A tasks worker --concurrency=2 --loglevel=INFO -E