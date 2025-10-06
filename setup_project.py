import os

# Define the folder structure
folders = [
    "app"
]

# Create directories
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Define the files to be created
files = [
    "app/__init__.py",
    "app/database.py",
    "app/models.py",
    "app/repository.py",
    "app/main.py",
    "requirements.txt",
    "README.md"
]

# Create empty files
for file in files:
    with open(file, "w") as f:
        pass  # just create empty files

print("✅ Project structure created successfully!")
