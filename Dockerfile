FROM python:3.10-alpine as base
FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --target=/install -r /requirements.txt


FROM base

COPY --from=builder /install /root/.local/lib/python3.10/site-packages
COPY src /app

WORKDIR /app

CMD ["python", "main.py", "--config_path", "./config.json"]
