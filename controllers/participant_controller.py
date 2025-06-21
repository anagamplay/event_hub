from core.data.event_list import event_list
from core.data.participant_list import participant_list
from core.exceptions.validation_error import ParticipantValidationError
from core.utils.most_common_elements import most_common_elements
from services.participant.participant_service import ParticipantService
from views.participant_view import ParticipantView

class ParticipantController:
    def __init__(self):
        self.participant_service = ParticipantService()
        self.participant_view = ParticipantView()
        self.participant_list = participant_list
        self.event_list = event_list
        
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
        except ParticipantValidationError as ve:
            self.participant_view.show_error_message(str(ve))
        except Exception as e:
            self.participant_view.show_error_message(f"Erro inesperado: {str(e)}")
            
    def list_participants(self):
        self.participant_view.show_title("Lista de Participantes")
        participants = self.participant_service.get_all_participants()
        for participant in participants:
            self.participant_view.show_participant(participant)

    def find_participant(self):
        self.participant_view.show_title("Buscar Participante")
        search_type = self.participant_view.get_input("Buscar por (1) ID ou (2) Nome? ")
        if search_type == '1':
            self.find_participant_by_id()
        elif search_type == '2':
            self.find_participant_by_name()
        else:
            self.participant_view.show_error_message("Opção inválida.")

    def find_participant_by_id(self):
        try:
            participant_id = int(self.participant_view.get_input("ID do participante: "))
            participant = self.participant_service.get_participant_by_id(participant_id)
            if participant:
                self.participant_view.show_participant(participant)
            else:
                self.participant_view.show_error_message("Participante não encontrado.")
        except ValueError:
            self.participant_view.show_error_message("ID inválido.")
            
    def find_participant_by_name(self):
        name = self.participant_view.get_input("Nome do participante: ").strip()
        results = self.participant_service.get_participants_by_name(name)
        if results:
            for participant in results:
                self.participant_view.show_participant(participant)
        else:
            self.participant_view.show_error_message("Nenhum participante encontrado com esse nome.")

    def participant_events(self):
        self.participant_view.show_title("Eventos do Participante")
        try:
            participant_id = int(self.participant_view.get_input("ID do participante: "))
            events = self.participant_service.get_events_by_participant(participant_id)
            if events:
                for i, event in enumerate(events, start=1):
                    self.participant_view.show_event(event, prefix=f"{i}")
            else:
                self.participant_view.show_error_message("Nenhum evento encontrado para este participante.")
        except ValueError:
            self.participant_view.show_error_message("ID inválido.")

    def most_active_participants(self):
        self.participant_view.show_title("Participantes Mais Ativos")
        participant_ids = self.participant_service.get_most_active_participants()
        for pid in participant_ids:
            participant = self.participant_service.get_participant_by_id(pid)
            if participant:
                self.participant_view.show_participant(participant)
            else:
                self.participant_view.show_error_message(f"Participante com ID {pid} não encontrado.")

    def remove_duplicate_participants(self):
        self.participant_view.show_title("Remover Participantes Duplicados")
        unique_participants = self.participant_service.get_unique_participants()
        for participant in unique_participants:
            self.participant_view.show_participant(participant)
            
    def update_participant(self):
        self.participant_view.show_title("Atualizar Participante")

        try:
            participant_id = int(self.participant_view.get_input("ID do participante a atualizar: "))
            participant = self.participant_service.get_participant_by_id(participant_id)

            if not participant:
                self.participant_view.show_error_message("Participante não encontrado.")
                return

            self.participant_view.show_participant(participant)

            self.participant_view.show_info_message("Deixe o campo vazio para manter o valor atual.")
            new_name = self.participant_view.get_input("Novo nome: ").strip()
            new_email = self.participant_view.get_input("Novo e-mail: ").strip()

            updated_participant = self.participant_service.update_participant(
                participant_id,
                name=new_name or participant.name,
                email=new_email or participant.email
            )

            if updated_participant:
                self.participant_view.show_success_message("Participante atualizado com sucesso!")
                self.participant_view.show_participant(updated_participant)
            else:
                self.participant_view.show_error_message("Erro ao atualizar participante.")

        except ValueError:
            self.participant_view.show_error_message("ID inválido.")
        except Exception as e:
            self.participant_view.show_error_message(f"Erro inesperado: {str(e)}")
            
    def remove_participant(self):
        self.participant_view.show_title("Remover Participante")

        try:
            participant_id = int(self.participant_view.get_input("ID do participante a remover: "))
            participant = self.participant_service.get_participant_by_id(participant_id)

            if not participant:
                self.participant_view.show_error_message("Participante não encontrado.")
                return

            confirm = self.participant_view.get_input(
                f"Tem certeza que deseja remover {participant.name}? (s/n): "
            ).strip().lower()

            if confirm == 's':
                success = self.participant_service.remove_participant(participant_id)
                if success:
                    self.participant_view.show_success_message("Participante removido com sucesso.")
                else:
                    self.participant_view.show_error_message("Erro ao remover participante.")
            else:
                self.participant_view.show_info_message("Remoção cancelada.")

        except ValueError:
            self.participant_view.show_error_message("ID inválido.")
        except Exception as e:
            self.participant_view.show_error_message(f"Erro inesperado: {str(e)}")
