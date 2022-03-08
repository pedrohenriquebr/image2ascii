import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
TEMP_DIR = os.path.join(ROOT_DIR, 'temp')
ENVIRONMENT = os.getenv('ENV','DEV')
PORT = int(os.getenv('PORT',5000))