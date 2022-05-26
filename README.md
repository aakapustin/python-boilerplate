# Python boilerplate

## Install

For production
```bash
$ pip install -r requirements.txt
```

For development
```bash
$ pip install -r requirements.dev.txt
```

## Configure

```bash
$ cp .env.example .env
```

Fill the environment variables in `.env`

## Launch

```bash
$ python src/main.py
```

## Count coverage

Run coverage
```bash
$ coverage run -m pytest
```

Make html report
```bash
$ coverage html
```

## Test

```bash
$ python -m pytest
```

## Build image
```bash
$ docker compose build
```

## Start container
```bash
$ docker compose up -d
```

## Stop and remove container
```bash
$ docker compose down
```
