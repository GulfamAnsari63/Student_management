from bson import ObjectId
from fastapi import APIRouter, HTTPException, Path, Query
from app.database.connection import db
from app.models.student_model import student_helper
from app.schemas.student_schema import StudentSchema, CreateStudentResponse
from app.schemas.student_schema import StudentSchema, UpdateStudentSchema
from app.schemas.student_schema import StudentSchema, ListStudentsResponse, StudentResponse
router = APIRouter()

@router.post("/students", response_model=CreateStudentResponse, status_code=201)
async def create_student(student: StudentSchema):
    student_data = student.dict()
    result = db.students.insert_one(student_data)
    return {"id": str(result.inserted_id)}

@router.get("/students",response_model=ListStudentsResponse, status_code=200)
async def list_students(country: str = Query(None), age: int = Query(None)):
    query = {}
    if country:
        query["address.country"] = country
    if age is not None:
        query["age"] = {"$gte": age}
    students = db.students.find(query)
    response_data = [
        StudentResponse(
            name=student.get("name", ""),
            age=student.get("age", 0),
        ) for student in students]
    return {"data": response_data}

@router.get("/students/{id}")
async def fetch_student( id: str = Path(...)):
    student = db.students.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)
    raise HTTPException(status_code=404, detail="Student not found")

@router.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: UpdateStudentSchema):
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    result = db.students.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.matched_count:
        return
    raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/students/{id}", response_model=dict)
async def delete_student(_id: str):
    result = db.students.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")
