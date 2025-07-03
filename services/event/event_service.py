from core.data.event_list import event_list
from models.event_model import Event
from services.event.event_validator import EventValidator

class EventService:
    def __init__(self):
        self.event_list = event_list
        self.event_validator = EventValidator()

    def create_event(self, name, description, date, location):
        self.event_validator.validate(
            name=name, description=description, date=date, location=location
        )

        last_id = max(map(lambda e: e['id'], self.event_list), default=0)
        new_id = last_id + 1

        new_event = Event(
            id=new_id,
            description=description,
            name=name,
            date=date,
            location=location,
            participants=[]
        )

        self.event_list.append(vars(new_event))
        return new_event

    def get_all_events(self):
        return list(map(lambda event: Event(**event), self.event_list))

    def get_event_by_id(self, event_id):
        event = next(filter(lambda e: e['id'] == event_id, self.event_list), None)
        return Event(**event) if event else None

    def update_event(self, event_id, name, description, date, location):
        self.event_validator.validate(
            name=name, description=description, date=date, location=location
        )

        event = next(filter(lambda e: e['id'] == event_id, self.event_list), None)
        if event:
            event.update({
                'name': name,
                'date': date,
                'location': location,
                'description': description
            })
            return Event(**event)
        return None

    def remove_event(self, event_id):
        index = next((i for i, e in enumerate(self.event_list) if e['id'] == event_id), None)
        if index is not None:
            del self.event_list[index]
            return True
        return False

    def get_events_with_few_participants(self, max_participants=2):
        return list(
            map(
                lambda event: Event(**event),
                filter(lambda e: len(e.get('participants', [])) <= max_participants, self.event_list)
            )
        )

    def add_participant_to_event(self, event_id, participant_id):
        event = next(filter(lambda e: e['id'] == event_id, self.event_list), None)
        if event:
            event.setdefault('participants', [])
            if participant_id not in event['participants']:
                event['participants'].append(participant_id)
            return True
        return False
