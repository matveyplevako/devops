FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV MODULE_NAME="app_python.main"
ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000

EXPOSE 8000

RUN adduser --disabled-password --shell /bin/sh --home /home/container_user container_user

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

USER container_user
WORKDIR /home/container_user

COPY --chown=container_user:container_user ./app_python /app_python
