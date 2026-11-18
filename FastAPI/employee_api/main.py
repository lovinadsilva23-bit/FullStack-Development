
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Employee Management API")

employees = {
    1: {"id": 1, "name": "John", "role": "Python Developer"},
    2: {"id": 2, "name": "Sarah", "role": "Technical Analyst"}
}


@app.get("/")
def home():
    return {"message": "Employee API is running"}


@app.get("/employees")
def get_employees():
    return list(employees.values())


@app.post("/employees", status_code=201)
def add_employee(employee: dict):
    employee_id = employee["id"]

    if employee_id in employees:
        raise HTTPException(status_code=409, detail="Employee already exists")

    employees[employee_id] = employee
    return {"message": "Employee added", "employee": employee}


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: dict):
    if employee_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee["id"] = employee_id
    employees[employee_id] = employee
    return {"message": "Employee updated", "employee": employee}


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    if employee_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")

    deleted = employees.pop(employee_id)
    return {"message": "Employee deleted", "employee": deleted}
