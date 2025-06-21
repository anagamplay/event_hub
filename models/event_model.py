class Event:
    def __init__(self, id: str, name: str, description: str, date: str, location: str, participants: list):
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.location = location
        self.participants = participants

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.name} | Descrição: {self.description} | Data: {self.date} | Local: {self.location}"
