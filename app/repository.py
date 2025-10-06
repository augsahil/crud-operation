from pymongo.errors import PyMongoError
from .models import Student

class StudentRepository:
    def __init__(self, db):
        # db is a pymongo.database.Database instance
        self.collection = db["students"]

    def insert(self, student: Student):
        """Insert a student document into the collection."""
        try:
            data = student.to_dict()
            result = self.collection.insert_one(data)
            print(f"Inserted student with _id: {result.inserted_id}")
        except PyMongoError as e:
            print(f"Error inserting student: {e}")
            raise

    def fetch_all(self):
        """Return list of Student objects for all documents."""
        try:
            cursor = self.collection.find()
            students = [Student.from_dict(doc) for doc in cursor]
            return students
        except PyMongoError as e:
            print(f"Error fetching students: {e}")
            raise

    def fetch_by_id(self, sid):
        """Fetch a single student by ID (the _id)."""
        try:
            doc = self.collection.find_one({"_id": sid})
            if doc:
                return Student.from_dict(doc)
            else:
                return None
        except PyMongoError as e:
            print(f"Error fetching student by id: {e}")
            raise

    def update(self, sid, student: Student):
        """Update an existing student (by sid)."""
        try:
            update_data = {
                "username": student.username,
                "email": student.email,
                "year": student.year,
                "department": student.department
            }
            result = self.collection.update_one({"_id": sid}, {"$set": update_data})
            print(f"Modified count: {result.modified_count}")
        except PyMongoError as e:
            print(f"Error updating student: {e}")
            raise

    def delete(self, sid):
        """Delete a student by sid."""
        try:
            result = self.collection.delete_one({"_id": sid})
            print(f"Deleted count: {result.deleted_count}")
        except PyMongoError as e:
            print(f"Error deleting student: {e}")
            raise
