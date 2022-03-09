# Image to ASCII

This API converts an image to ASCII art style

## Prequisites

-  Python 3.9+
-  PNPM v6.30+
-  Node v14+


## Installation

Install the packages:

```bash
$ pip install -r requirements.txt
```

Install the frontend packages:

```bash
$ cd frontend
$ pnpm install
```

## Running

Start the backend

```bash
$ python main.py
```

or if you prefer using uvicorn

```bash
$ uvicorn main:app --reload
```

> Install uvicorn before via pip: pip install uvicorn


Start the frontend

```bash
$ cd frontend
$ pnpm run start
```

Check the link `http://localhost:3000` on browser and Voilà


## Configuration

You can set environment vars on `.env`

```dotenv
ENV=DEV # PROD for production
PORT=5000 # the listening port
```

All these vars are globally loaded from `config.py` script:

```python
import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
TEMP_DIR = os.path.join(ROOT_DIR, 'temp')
ENVIRONMENT = os.getenv('ENV','DEV')
PORT = int(os.getenv('PORT',5000))
```


