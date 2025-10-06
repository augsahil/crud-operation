class Student:
    def __init__(self, sid, username, email, year, department):
        self.sid = sid
        self.username = username
        self.email = email
        self.year = year
        self.department = department

    def to_dict(self):
        return {
            "_id": self.sid,
            "username": self.username,
            "email": self.email,
            "year": self.year,
            "department": self.department
        }

    @classmethod
    def from_dict(cls, d):
        # d is a dict coming from MongoDB
        return cls(
            sid = d.get("_id"),
            username = d.get("username"),
            email = d.get("email"),
            year = d.get("year"),
            department = d.get("department")
        )

    def __repr__(self):
        return (
            f"Student(sid={self.sid}, username={self.username}, "
            f"email={self.email}, year={self.year}, department={self.department})"
        )
