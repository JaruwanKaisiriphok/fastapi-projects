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
    return {'message': f'Blog type {type}'}

@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message':f'Blog with id {id}'}


d = [
    {"Name": "Pele Kanaphon", "date": date.today(), "Age": 17},
    {"Name": "Por Jaruwan ", "date": date.today(), "Age": 52},
]

@app.get('/')
async def MyData():    
    json_str = json.dumps(d, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')