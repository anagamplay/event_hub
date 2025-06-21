class Participant:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.name} | Email: {self.email}"
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(id=data['id'], name=data['name'], email=data['email'])
