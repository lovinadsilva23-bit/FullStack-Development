from fastapi import FastAPI

app = FastAPI(title="Employee Management API")


@app.get("/")
def home():
    return {"message": "Welcome to Employee Management API"}


@app.get("/employees")
def get_employees():
    return [
        {"id": 1, "name": "John", "role": "Python Developer"},
        {"id": 2, "name": "Sarah", "role": "Technical Analyst"}
    ]

@app.post("/employees")
def add_employee(employee: dict):
    return {
        "message": "Employee added successfully",
        "employee": employee
    }