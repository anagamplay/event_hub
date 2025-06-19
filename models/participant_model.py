class Participant:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.name} | Email: {self.email}"
    
    def set_id(self, id):
        self.id = id
        return self