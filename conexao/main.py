from fastapi import FastAPI
from contextlib import asynccontextmanager
from conexao.controllers import post
from conexao.database import database, metadata, engine

# cria tabelas
metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(post.router)