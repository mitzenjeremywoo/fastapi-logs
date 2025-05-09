from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class Employee(BaseModel):
    name: str
    id: int

app = FastAPI()

@app.get("/healthz")
def read_root():
    return "OK:" + str(datetime.now(timezone.utc))

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    
# pass json payload 
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# return json output automatically 
@app.get("/employee/{id}")
def read_item(id: int):
    return Employee(name="Alice", id=id)

# handling post requests
@app.post("/employee/{id}")
def read_item(id: int, employee: Employee):
    print("created employee")
    return employee

# handling post requests
@app.delete("/employee/{id}")
def read_item(id: int, employee: Employee):
    if id == 1:
        print("deleted employee")
        return employee
    else:
        raise HTTPException(status_code=404, detail="User not found")

        
    

