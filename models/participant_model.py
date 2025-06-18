class Participant:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
    
    def to_string(self):
        return f"ID: {self.id} | Nome: {self.name} | Email: {self.email}"