from fastapi import FastAPI
from fastapi.responses import HTMLResponse

posts = [
     {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is awesome",
        "content": "This framework makes it super fast to build APIs",
        "date_posted": "June 1, 2024"
     },
     {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is great",
        "content": "Python is a versatile programming language.",
        "date_posted": "June 2, 2024"
     }
]

app = FastAPI()

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"