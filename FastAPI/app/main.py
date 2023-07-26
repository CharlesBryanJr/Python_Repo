'''main.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304

from typing import Optional
from random import randrange
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

my_posts = [{"username": "charles_bryan", "content": "First post", "id": 1},
{"username": "charles_bryan", "content": "Second post", "id": 2}]

class Post(BaseModel):
    username: str
    content: str
    published: bool = True
    rating: Optional[int] = None

try:
    conn = psycopg2.connect(host='localhost',
            database = 'fastapi',
            user = 'postgress',
            password = 'PGcab312.jr02',
            cursor_factory = RealDictCursor)
    cursor = conn.cursor()
    print("Database connection: Sucess")
except:
    print("Database connection: Failure")

def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post

def find_post_idx(id):
    for idx, post in enumerate(my_posts):
        if post['id'] == id:
            return idx

@app.get("/posts")
def get_posts():
    return {"Post Data": my_posts}

@app.post("/posts_1", status_code=status.HTTP_201_CREATED)
def create_post_1(payload: dict = Body(...)):
    print(payload)
    return {"post_created": f"username: {payload['username']}, content: {payload['content']}"}

@app.post("/posts_2", status_code=status.HTTP_201_CREATED)
def create_post_2(post: Post):
    print(" ")
    print("username:", post.username)
    print("content:", post.content)
    print("published:", post.published)
    print("rating:", post.rating)
    print(" ")
    post.dict()
    return {"new_post": post}

@app.post("/posts_3", status_code=status.HTTP_201_CREATED)
def create_post_3(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"Post Data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Post {id}, Not Found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Post Data": f"Post {id}, Not Found"}
    return {"Post Data": post}

@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    idx = find_post_idx(id)
    if idx is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Post {id}, Not Found")

    my_posts.pop(idx)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/post/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, post: Post):
    idx = find_post_idx(id)
    if idx is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Post {id}, Not Found")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[idx] = post_dict
    return {"Post Data": my_posts[idx]}
    