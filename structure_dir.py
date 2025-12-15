import os

# Define the directory structure
structure = {
    "retail-analytics-backend_2": {
        "app": {
            "__init__.py": "",
            "main.py": "",
            "database.py": "",
            "models.py": "",
            "routes": {
                "__init__.py": "",
                "visitors.py": "",
                "cashier.py": "",
                "heatmap.py": "",
                "predictions.py": "",
                "chatbot.py": "",
            },
            "utils": {
                "demo_sender.py": "",
            }
        },
        "requirements.txt": "",
        ".env": "",
        ".gitignore": "",
        "railway.toml": "",
        "Procfile": "",
    }
}

def create_structure(base_path, structure):
    """Recursively create directory structure and empty files"""
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        
        if isinstance(content, dict):
            # It's a directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # It's a file
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

# Create the structure starting from current directory
create_structure(".", structure)

print("Directory structure created successfully!")
print("Created:")
print("retail-analytics-backend/")
print("├── app/")
print("│   ├── __init__.py")
print("│   ├── main.py")
print("│   ├── database.py")
print("│   ├── models.py")
print("│   ├── routes/")
print("│   │   ├── __init__.py")
print("│   │   ├── visitors.py")
print("│   │   ├── cashier.py")
print("│   │   ├── heatmap.py")
print("│   │   ├── predictions.py")
print("│   │   └── chatbot.py")
print("│   └── utils/")
print("│       └── demo_sender.py")
print("├── requirements.txt")
print("├── .env")
print("├── .gitignore")
print("├── railway.toml")
print("└── Procfile")