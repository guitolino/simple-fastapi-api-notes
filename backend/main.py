from fastapi import FastAPI

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield

app = FastAPI(
    title="simple fastapi notes api",
    version="0.1.1",
    lifespan=lifespan
)

