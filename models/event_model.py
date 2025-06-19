class Event:
    def __init__(self, event_id: str, name: str, description: str, date: str, location: str):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.date = date
        self.location = location

    def __str__(self):
        return f"ID: {self.event_id} | Nome: {self.name} | Descrição: {self.description} | Data: {self.date} | Local: {self.location}"
    