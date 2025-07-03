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

        last_id = max(map(lambda p: p['id'], self.participant_list), default=0)
        new_id = last_id + 1

        new_participant = Participant(id=new_id, name=name, email=email)
        self.participant_list.append(vars(new_participant))
        return new_participant

    def get_all_participants(self):
        return self.participant_list

    def get_participant_by_id(self, participant_id):
        participant = next(
            filter(lambda p: p['id'] == participant_id, self.participant_list), None)
        return Participant.from_dict(participant) if participant else None

    def get_participants_by_name(self, name):
        name_lower = name.lower()
        return list(filter(lambda p: name_lower in p['name'].lower(), self.participant_list))

    def get_events_by_participant(self, participant_id):
        return list(filter(lambda e: participant_id in e['participants'], self.event_list))

    def get_most_active_participants(self) -> list[Participant]:
        all_participants = [
            pid for event in self.event_list for pid in event['participants']]
        most_common_ids = most_common_elements(all_participants)
        participants_by_id = {
            p['id']: Participant.from_dict(p)
            for p in self.participant_list
        }
        return list(filter(None, map(lambda pid: participants_by_id.get(pid), most_common_ids)))

    def get_unique_participants(self):
        seen_ids = set()
        return list(filter(
            lambda p: not (p['id'] in seen_ids or seen_ids.add(p['id'])),
            map(lambda p: p, self.participant_list)
        ))

    def update_participant(self, participant_id, name, email):
        for participant in self.participant_list:
            if participant['id'] == participant_id:
                self.participant_validator.validate(name=name, email=email)
                participant['name'] = name
                participant['email'] = email
                return participant
        return None

    def remove_participant(self, participant_id):
        index = next((i for i, p in enumerate(self.participant_list) if p['id'] == participant_id), None)
        if index is not None:
            del self.participant_list[index]
            return True
        return False
