from core.data.participant_list import participant_list
from models.participant_model import Participant
from services.participant.participant_validator import ParticipantValidator

class ValidationError(Exception):
    pass

class ParticipantService:
    def __init__(self):
        self.participant_list = participant_list
        self.participant_validator = ParticipantValidator()

    def create_participant(self, name, email):
        self.participant_validator.validate(name=name, email=email)
        
        last_id = max([p['id'] for p in self.participant_list], default=0)
        new_id = last_id + 1
        new_participant = Participant(id=new_id, name=name, email=email)

        self.participant_list.append({
            'id': new_participant.id,
            'name': new_participant.name,
            'email': new_participant.email
        })

        return new_participant