from fastapi import FastAPI
from router import router as rout
from logs.logger import logit
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

app.add_middleware(BaseHTTPMiddleware, dispatch=logit)

app.include_router(rout)
