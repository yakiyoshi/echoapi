FROM python:3.12.6


COPY ./app/ /usr/src/app/
COPY ./requirements.txt /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--port", "5000"]
