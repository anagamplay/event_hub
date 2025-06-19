from core.data.event_list import event_list
from core.data.participant_list import participant_list
from core.utils.most_common_elements import most_common_elements
from services.participant.participant_service import ParticipantService
from views.participant_view import ParticipantView

class ParticipantController:
    def __init__(self):
        self.participant_service = ParticipantService()
        self.participant_view = ParticipantView()
        
    @staticmethod
    def list_participants():
        for participant in participant_list:
            print(
                f"ID: {participant['id']} | Nome: {participant['name']} | Email: {participant['email']}")

    @staticmethod
    def search_participant(user_id):
        return [participant for participant in participant_list if participant['id'] == user_id]

    @staticmethod
    def participant_events(participant_id):
        participant_events = []
        for event in event_list:
            list_event_participants = event['participants']
            if participant_id in list_event_participants:
                participant_events.append(event)
        return participant_events

    @staticmethod
    def most_active_participants():
        events_participants = []

        for event in event_list:
            events_participants.extend(event['participants'])

        return most_common_elements(events_participants)

    @staticmethod
    def remove_duplicate_participants():
        unique_participants = []
        seen_ids = set()

        for participant in participant_list:
            if participant['id'] not in seen_ids:
                unique_participants.append(participant)
                seen_ids.add(participant['id'])
        return unique_participants

    @staticmethod
    def events_with_few_participants():
        few_participants_events = []

        for event in event_list:
            if len(event['participants']) < 3:
                few_participants_events.append(event)
        return few_participants_events

    def add_participant(self):
        self.participant_view.show_title('Cadastro de Participante')
        try:
            name = self.participant_view.get_input("Nome: ")
            email = self.participant_view.get_input("E-mail: ")
            new_participant = self.participant_service.create_participant(name, email)
            if (new_participant):
                self.participant_view.show_success_message("Cadastro realizado com sucesso!")
            else:
                self.participant_view.show_error_message("Erro ao realizar cadastro.")
        except Exception as e:
            self.participant_view.show_error_message(f"Erro inesperado: {str(e)}")
