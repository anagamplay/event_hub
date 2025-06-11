from events.event_list import event_list

class EventService:
    def list_events():
        print("\neventos disponíveis:")
        for event in event_list:
            print(f"ID: {event['id']} | nome: {event['name']} | data: {event['date']} | local: {event['location']}")

    def list_event_participants(participants, event_id):
        for evento in event_list:
            if evento['id'] == event_id:
                print(evento['participants'])
                for participante in participants:
                    for i in evento['participants']:
                        if participante['id'] == i:
                            print(participante['name'])

    def add_event(new_event):
        event_list.append(new_event)
