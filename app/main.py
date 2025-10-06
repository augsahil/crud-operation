from .database import MongoDBClient
from .models import Student
from .repository import StudentRepository

def main():
    # Initialize and connect to MongoDB
    mongo_client = MongoDBClient()

    try:
        mongo_client.connect()  # establishes connection
        repo = StudentRepository(mongo_client.db)  # pass database instance

        print("\n=== 🟢 INSERT STUDENTS ===")
        s1 = Student(sid=1, username="alice", email="alice@example.com", year=2, department="CSE")
        s4 = Student(sid=4, username="bob", email="bob@example.com", year=4, department="ECE")

        repo.insert(s1)
        repo.insert(s4)

        print("\n=== 📋 FETCH ALL STUDENTS ===")
        students = repo.fetch_all()
        for st in students:
            print(st)

        print("\n=== 🔍 FETCH STUDENT BY ID = 1 ===")
        student = repo.fetch_by_id(1)
        print(student)

        print("\n=== ✏️ UPDATE STUDENT ID = 2 ===")
        s4_updated = Student(sid=4, username="bob", email="bob_updated@example.com", year=4, department="ECE")
        repo.update(4, s4_updated)
        print("After update:", repo.fetch_by_id(4))

        print("\n=== ❌ DELETE STUDENT ID = 1 ===")
        repo.delete(1)
        print("Remaining students:", repo.fetch_all())

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        mongo_client.close()


if __name__ == "__main__":
    main()
