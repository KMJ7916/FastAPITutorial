from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel

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
@app.get("/helllo")
def get_hello():
    return {"Hello LikeLion!"}


(2)
@app.get("/user/{user_id}")
def get_user(user: User):
    return {"name":user.name, "email":user.email}

class Student(BaseModel):
    name: str
    age: int
    email : str
    
# (3)    
@app.post("/students")
def informationStudent(student:Student):
    return{"name":student.name, "email":student.email}

# (4)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "project deleted"}

# (5)
@app.get("/age/{age}")
def get_age(age: int,user:User):
    if age<18:
        return {"message":"You are under 18."}
    else:
        return {"message":"You are an adult."}


# (6)
@app.post("/create_student", status_code=status.HTTP_201_CREATED)
def create_student(stduent :Student):
    return {"message": "User created successfully", "name": stduent.name}


# (7)
@app.get("/students")
def studentList(stduent :Student):
    return {"students": [{"name": "Alice", "email": "alice@example.com"}, {"name": "Bob", "email": "bob@example.com"}]}
    
# (8)
@app.get("/user/{user_id}",response_model=User)
def get_user(user_id: int):
    return {"name":"Alice", "age":25}


# (9)
@app.get("/serch")
def searchKeyword(q :str):
        return {"results": ["item1", "item2", "item3"], "query": q}
    
# (10)
@app.post("error")
def custom_error():
    raise HTTPException(status_code=400, detail="Invalid request")