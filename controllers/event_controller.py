from core.data.event_list import event_list

class EventController:
    def list_events(self):
        for event in event_list:
            print(f"ID: {event['id']} | nome: {event['name']} | data: {event['date']} | local: {event['location']}")

    def list_event_participants(self, participants, event_id):
        for evento in event_list:
            if evento['id'] == event_id:
                print(evento['participants'])
                for participante in participants:
                    for i in evento['participants']:
                        if participante['id'] == i:
                            print(participante['name'])

    def add_event(self, new_event):
        last_id = max([e['id'] for e in event_list], default=0)
        new_event["id"] = last_id + 1
        event_list.append(new_event)