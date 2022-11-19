FROM python:3-slim as python
ENV PYTHONUNBUFFERED=true

RUN pip install poetry==1.1.12

WORKDIR /code
COPY . /code

RUN poetry config virtualenvs.create false &&\
    poetry install --no-interaction --no-ansi -vvv

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]