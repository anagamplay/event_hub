from collections import Counter
from events.event_list import event_list
from participants.participant_list import participant_list
from utils import most_common_elements


class ParticipantsService:
    def search_participant(user_id):
        return [participant for participant in participant_list if participant['id'] == user_id]

    def participant_events(participant_id):
        participant_events = []
        for event in event_list:
            list_event_participants = event['participants']
            if participant_id in list_event_participants:
                participant_events.append(event)
        return participant_events

    def most_active_participants():
        events_participants = []

        for event in event_list:
            events_participants.extend(event['participants'])

        return most_common_elements(events_participants)

    def remove_duplicate_participants():
        unique_participants = []
        seen_ids = set()

        for participant in participant_list:
            if participant['id'] not in seen_ids:
                unique_participants.append(participant)
                seen_ids.add(participant['id'])
        return unique_participants

    def events_with_few_participants():
        few_participants_events = []

        for event in event_list:
            if len(event['participants']) < 3:
                few_participants_events.append(event)
        return few_participants_events
