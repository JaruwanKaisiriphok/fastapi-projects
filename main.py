from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

from fastapi import Response
from datetime import date

import json

app = FastAPI()

@app.get('/blog/MyName')
def index():
    return {'message':'Hello Por !!! ...'}

@app.get('/blog/all')
def get_blog():
    return {'message':' All blogs provide'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{typr}')
def get_blog_type(typr: BlogType):
    return {'message': f'Blog type {typr}'}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message':f'Blog with id {id}'}


d = [
    {"id": 1, "name": "Pele Kanaphon", "date": date.today().isoformat(), "age": 17},
    {"id": 2, "name": "Por Jaruwan", "date": date.today().isoformat(), "age": 52},
]

@app.get("/")
async def MyData():
    # ห่อ array d ด้วย key "data"
    result = {
        "items": d
    }
    json_str = json.dumps(result, indent=4, default=str)
    return Response(content=json_str, media_type="application/json")
