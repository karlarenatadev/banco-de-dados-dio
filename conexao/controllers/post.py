import sqlalchemy as sa
from conexao.database import metadata

from fastapi import APIRouter

router = APIRouter()

@router.get("/posts")
def listar_posts():
    return {"message": "lista de posts"}

posts = sa.Table('posts', metadata, sa.Column('id', sa.Integer, primary_key=True),
                 sa.Column('title', sa.String(150), nullable=False, unique=True),
                 sa.Column('content', sa.String(500), nullable=False),
                 sa.Column('published_at', sa.DateTime, nullable=True),
                 sa.Column('published', sa.Boolean, default=False)
                 )
