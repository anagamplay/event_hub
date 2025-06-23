from core.data.event_list import event_list
from core.data.participant_list import participant_list
from core.utils.most_common_elements import most_common_elements
from models.participant_model import Participant
from services.participant.participant_validator import ParticipantValidator

class ParticipantService:
    def __init__(self):
        self.participant_list = participant_list
        self.participant_validator = ParticipantValidator(
            self.participant_list)
        self.event_list = event_list

    def create_participant(self, name, email):
        self.participant_validator.validate(name=name, email=email)
        self.participant_validator.validate_email_not_in_use(email)
        last_id = max([p['id'] for p in self.participant_list], default=0)
        new_id = last_id + 1
        new_participant = Participant(id=new_id, name=name, email=email)
        self.participant_list.append({
            'id': new_participant.id,
            'name': new_participant.name,
            'email': new_participant.email
        })
        return new_participant

    def get_all_participants(self):
        return self.participant_list

    def get_participant_by_id(self, participant_id):
        for participant in self.participant_list:
            if participant_id == participant['id']:
                return Participant.from_dict(participant)
        return None

    def get_participants_by_name(self, name):
        return [
            participant for participant in self.participant_list
            if name.lower() in participant['name'].lower()
        ]

    def get_events_by_participant(self, participant_id):
        return [event for event in event_list if participant_id in event['participants']]

    def get_most_active_participants(self) -> list[Participant]:
        all_participants = []
        most_common_ids = most_common_elements(all_participants)
        participants_by_id = {p['id']: Participant.from_dict(p) for p in self.participant_list}
        return [participants_by_id[pid] for pid in most_common_ids if pid in participants_by_id]

    def get_unique_participants(self):
        unique = []
        seen_ids = set()
        for participant in self.participant_list:
            if participant['id'] not in seen_ids:
                unique.append(Participant.from_dict(participant))
                seen_ids.add(participant['id'])
        return unique

    def update_participant(self, participant_id, name, email):
        for participant in self.participant_list:
            if participant['id'] == participant_id:
                self.participant_validator.validate(name=name, email=email)

                participant['name'] = name
                participant['email'] = email
                return participant
        return None
    
    def remove_participant(self, participant_id):
        for index, participant in enumerate(self.participant_list):
            if participant['id'] == participant_id:
                del self.participant_list[index]
                return True
        return False
