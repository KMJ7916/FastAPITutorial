from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: int

@app.get("/user/{user_id}", response_model=User)
def get_user(user_id: int):
    # 실제 구현에서는 데이터베이스에서 사용자 정보를 조회하겠지만, 여기서는 예시 데이터를 사용합니다.
    # return User(name="Alice", age=30)
    return {"name":"Alice", "age":30 , "email":"hello@example.com"}


# -------연습문제-------
# (1)
class Event(BaseModel):
    name: str
    date: datetime
    participant: int
    
@app.post("/event")
def add_event(event:Event):
    return {"message": "Event registered successfully", "event": event}
    
    
# (2)
class Book(BaseModel):
    title: str
    author: str
    date: datetime
    
@app.post("/book")
def book(book:Book):
    return {"message": "Book recorded successfully", "book": book}

    
# (3)    
class Likelion(BaseModel):
    name: str
    email: EmailStr
    date: datetime
    
@app.post("/member")
def member(member:Likelion):
    return {"message": "Member registered successfully", "member": member}


# (4)
class Food(BaseModel):
    menu: str
    price: float
    date: datetime
    
@app.post("/schoolfood")
def schoolFood(food:Food):
    return {"message": "Menu registered successfully", "menu": food}


# (5)
class student(BaseModel):
    name: str
    subject: str
    max_participant: int
    
@app.post("/studyGroup")
def studyGroup(student:student):
    return {"message": "Study group created successfully", "group": student}