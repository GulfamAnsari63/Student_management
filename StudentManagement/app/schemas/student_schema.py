from pydantic import BaseModel, Field
from typing import List, Optional

class AddressSchema(BaseModel):
    city: str
    country: str

class StudentSchema(BaseModel):
    name: str
    age: int
    address: AddressSchema

class CreateStudentResponse(BaseModel):
    id: str

class StudentResponse(BaseModel):
    name: str
    age: int
class ListStudentsResponse(BaseModel):
    data: List[StudentResponse]

class UpdateStudentSchema(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[AddressSchema]
