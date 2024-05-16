from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    # price: float
    # tax: float = None
    


# @app.post("/items/")
# def create_item(item: Item):
#     return {"name": item.name, "price": item.price}

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id, "name": "Sample Item"}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, "name": item.name, "price": item.price}

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     return {"message": "Item deleted"}


# @app.get("/like/lion")
# def read_root():
#     return {"응답":"멋쟁이 사자처럼"}

# --------- 연습문제 -----------
class Student(BaseModel):
    student_id:int
    name:str
    email: str
    
    
@app.get("/student/{student_id}")
def searchStudent(student_id: int):
    return {"student_id": student_id, "name": "김멋사", "email": "kimmutsa@example.com"}

@app.post("/projects/")
def createStudent(item: Item):
    return {"name": item.name, "description": item.description}

@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    return {"message": "project deleted"}


# @app.get("/") #데코레이터로 get으로 들어오면(post,delete)/라우팅 경로
# def read_root():
#     return {"Hello": "World"} #뷰라고 생각하면 됌

# @app.get("/items/{item_id}") # == /products/<int:item_id>/ 주소가 엔드포인트
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q":"likelion"}
