from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/MyName')
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


