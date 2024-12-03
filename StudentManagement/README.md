# Student Management System

## 📜 Description
A backend application for managing student records, built using **FastAPI** and **MongoDB Atlas**. This system provides RESTful APIs to create, fetch, update, delete, and list student records.

## 🚀 Features
- CRUD operations for student records.
- MongoDB Atlas integration for seamless cloud-based database management.
- Structured project layout following best practices.
- Scalable and easy-to-maintain architecture.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **Database:** MongoDB (Atlas)
- **HTTP Server:** Gunicorn with Uvicorn workers

---

## 📂 Project Structure
--**student-management-system/**
- ├── **app/**.
- │   ├── **main.py**                # Entry point of the application
- │   ├── **models/**                # Database models
- │   │   ├── **student_model.py**
- │   ├── **routes/**               # API route definitions
- │   │   ├── **student_routes.py**
- │   ├── **database/**             # Database connection
- │   │   ├── **connection.py**
- │   ├── **schemas/**             # Data validation schemas
- │       ├── **student_schema.py**
- ├── **requirements.txt**          # Python dependencies
- ├── **README.md**                 # Project documentation

---

## ⚡ Quick Start
- **1️⃣ Clone the Repository**
- **2️⃣ Set Up Virtual Environment (Optional but Recommended)**
- **3️⃣ Install Dependencies**
- **4️⃣ Configure MongoDB Atlas**
- **Set up a free MongoDB cluster on MongoDB Atlas.**
- **Update your MongoDB connection URI in connection.py**
- **5️⃣ Run the Application**
- **6️⃣ Access the API**
- *The application will be running at: http://127.0.0.1:8000*
- **Swagger Docs: http://127.0.0.1:8000/docs**

---

## 🧪 API Endpoints 
- *Method*	- *Endpoint*	       - *Description*
- **POST**	 - **/students**      - **Add a new student record**
- **GET**   	- **/students**       - **Get all student records**
- **GET**	    - **/students/{id}**	- **Get a specific student record**
- **PUT**   	- **/students/{id**	  - **Update a student record**
- **DELETE**	- **/students/{id}**	- **Delete a student record**
