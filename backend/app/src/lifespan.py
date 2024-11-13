__all__ = ["lifespan"]
from fastapi import FastAPI


async def lifespan(app: FastAPI):
    # Paste your code here
    yield
