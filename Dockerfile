FROM python:3.10.2

WORKDIR /code

RUN pip install --upgrade pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code

EXPOSE 80

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
