from core.data.event_list import event_list
from models.event_model import Event
from services.event.event_validator import EventValidator

class EventService:
    def __init__(self):
        self.event_list = event_list
        self.event_validator = EventValidator()

    def create_event(self, name, description, date, location):
        self.event_validator.validate(name=name, description=description, date=date, location=location)

        last_id = max([e['id'] for e in self.event_list], default=0)
        new_id = last_id + 1

        new_event = Event(id=new_id, description=description, name=name, date=date, location=location, participants=[])

        self.event_list.append({
            'id': new_event.id,
            'name': new_event.name,
            'date': new_event.date,
            'description': new_event.description,
            'location': new_event.location,
            'participants': []
        })

        return new_event

    def get_all_events(self):
        return [Event(**event) for event in self.event_list]

    def get_event_by_id(self, event_id):
        for event in self.event_list:
            if event['id'] == event_id:
                return Event(**event)
        return None

    def update_event(self, event_id, name, description, date, location):
        self.event_validator.validate(name=name, description=description, date=date, location=location)

        for event in self.event_list:
            if event['id'] == event_id:
                event['name'] = name
                event['date'] = date
                event['location'] = location
                return Event(**event)
        return None

    def remove_event(self, event_id):
        for index, event in enumerate(self.event_list):
            if event['id'] == event_id:
                del self.event_list[index]
                return True
        return False

    def get_events_with_few_participants(self, max_participants=2):
        few_participants = []
        for event in self.event_list:
            if len(event.get('participants', [])) <= max_participants:
                few_participants.append(Event(**event))
        return few_participants
    
    def add_participant_to_event(self, event_id, participant_id):
        for event in self.event_list:
            if event['id'] == event_id:
                if 'participants' not in event:
                    event['participants'] = []
                if participant_id not in event['participants']:
                    event['participants'].append(participant_id)
                return True
        return False
