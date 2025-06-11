from collections import Counter
from events.event_list import event_list
from participants.participant_list import participant_list
from utils import most_common_elements

class ParticipantsService:
    def search_participant(id):
        return [participant for participant in participant_list if participant['id'] == id]

    def participant_events(participant_id):
        for event in event_list:
            list_event_participants = event['participants']
            if participant_id in list_event_participants:
                print(event['name'])

    def most_active_participants():
        events_participants = []

        for event in event_list:
            events_participants.extend(event['participants'])

        return most_common_elements(events_participants)
