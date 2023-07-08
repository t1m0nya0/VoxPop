from pydantic import BaseModel


class Category(BaseModel):
    positive: bool
    negative: bool

class Comment(BaseModel):
    text: str
    category: Category