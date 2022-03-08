from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from config import ENVIRONMENT

import routes
import handlers

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "*"
]

app.add_exception_handler(StarletteHTTPException,
                          handlers.custom_http_exception_handler)

app.post('/api/uploadfile/')(routes.upload_image)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if ENVIRONMENT == 'PROD':
    app.mount("/", StaticFiles(directory="./frontend/build",
              html=True), name="static")
