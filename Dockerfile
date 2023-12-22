FROM python:3.11.7

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

RUN pip install fastapi uvicorn

COPY . /code

CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app" ]