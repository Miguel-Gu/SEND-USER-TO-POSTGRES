FROM python:3.9

WORKDIR /sendToPostgres

COPY ./requirements.txt /sendToPostgres/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /sendToPostgres/requirements.txt

COPY ./app /sendToPostgres/app

ENV DB_CREDENTIALS='{"db_user":"postgres","db_pass":"suasenha","db_host":"ipdobanco"}'

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]