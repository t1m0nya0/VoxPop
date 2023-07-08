from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from .models import Comment

templates = Jinja2Templates(directory="templates")

app = FastAPI()

comments = [
    {
        "text": "saaaaalam",
        "category": {
            "positive": True,
            "negative": False
        }
    }
]


@app.get("/comments")
def get_comments(request: Request, page: int = 1, limit: int = 10):
    start_index = (page - 1) * limit
    end_index = start_index + limit
    paginated_comments = comments[start_index:end_index]
    return {"paginated_comments": paginated_comments}


@app.post("/comments")
def create_comment(comment: Comment):
    positive_category = comment.category.positive
    negative_category = comment.category.negative
    comments.append({
        "text": comment.text,
        "category": {
            "positive": positive_category,
            "negative": negative_category
        }
    })

    return {"message": "Item created"}
