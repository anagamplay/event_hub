from core.exceptions.participant_validation_error import ParticipantValidationError
from services.event.event_service import EventService
from services.participant.participant_service import ParticipantService
from views.participant_view import ParticipantView

class ParticipantController:
    def __init__(self):
        self.participant_service = ParticipantService()
        self.participant_view = ParticipantView()
        self.event_service = EventService()

    def add_participant(self):
        self.participant_view.show_title('Cadastro de Participante')
        try:
            name = self.participant_view.get_input("Nome: ")
            email = self.participant_view.get_input("E-mail: ")
            participant = self.participant_service.create_participant(name, email)
            
            selected_event_ids = self._select_events_for_participant()

            if not selected_event_ids:
                self.participant_view.show_error_message("O participante deve estar inscrito em pelo menos um evento.")
                return

            self._add_to_events(participant.id, selected_event_ids)
            
            self.participant_view.show_success_message("Cadastro realizado com sucesso!")
            self.participant_view.show_participant(participant)
            
        except (ParticipantValidationError, Exception) as e:
            self._handle_error(e)
            
    def list_participants(self):
        self.participant_view.show_title("Lista de Participantes")
        for participant in self.participant_service.get_all_participants():
            self.participant_view.show_participant(participant)

    def find_participant(self):
        self.participant_view.show_title("Buscar Participante")
        option = self.participant_view.get_input("Buscar por (1) ID ou (2) Nome? ")
        
        if option == '1':
            participant = self._find_by_id()
            self.participant_view.show_participant(participant)
        elif option == '2':
            self._find_by_name()
        else:
            self.participant_view.show_error_message("Opção inválida.")

    def participant_events(self):
        self.participant_view.show_title("Eventos do Participante")
        try:
            participant_id = self._get_participant_id()
            events = self.participant_service.get_events_by_participant(participant_id)
            
            if events:
                for event in events:
                    self.participant_view.show_event(event)
            else:
                self.participant_view.show_error_message("Nenhum evento encontrado para este participante.")
                
        except Exception as e:
            self._handle_error(e)

    def most_active_participants(self):
        self.participant_view.show_title("Participantes Mais Ativos")
        participants = self.participant_service.get_most_active_participants()
        for participant in participants:
            self.participant_view.show_participant(participant)

    def remove_duplicate_participants(self):
        self.participant_view.show_title("Remover Participantes Duplicados")
        participants = self.participant_service.get_unique_participants()
        for participant in participants:
            self.participant_view.show_participant(participant)
            
    def update_participant(self):
        self.participant_view.show_title("Atualizar Participante")
        try:
            participant_id = self._get_participant_id()
            participant = self.participant_service.get_participant_by_id(participant_id)
            if not participant:
                self.participant_view.show_error_message("Participante não encontrado.")
                return

            self.participant_view.show_participant(participant)
            self.participant_view.show_info_message("Deixe em branco para manter o valor atual.")

            new_name = self.participant_view.get_input("Novo nome: ").strip()
            new_email = self.participant_view.get_input("Novo e-mail: ").strip()

            updated_participant = self.participant_service.update_participant(
                participant_id,
                name=new_name or participant.name,
                email=new_email or participant.email
            )

            self.participant_view.show_success_message("Participante atualizado com sucesso!")
            self.participant_view.show_participant(updated_participant)

        except (ParticipantValidationError, Exception) as e:
            self._handle_error(e)
            
    def remove_participant(self):
        self.participant_view.show_title("Remover Participante")
        try:
            participant_id = self._get_participant_id()
            participant = self.participant_service.get_participant_by_id(participant_id)
            if not participant:
                self.participant_view.show_error_message("Participante não encontrado.")
                return

            confirm = self.participant_view.get_input(
                f"Tem certeza que deseja remover {participant.name}? (s/n): "
            ).strip().lower()

            if confirm == 's':
                self.participant_service.remove_participant(participant_id)
                self.participant_view.show_success_message("Participante removido com sucesso.")
            else:
                self.participant_view.show_info_message("Remoção cancelada.")

        except Exception as e:
            self._handle_error(e)
            
    def add_participant_to_event(self):
        self.participant_view.show_title("Adicionar Participante a Evento")
        try:
            participant_id = self._get_participant_id()
            participant = self.participant_service.get_participant_by_id(participant_id)
            if not participant:
                self.participant_view.show_error_message("Participante não encontrado.")
                return

            selected_event_ids = self._select_events_for_participant()
            if not selected_event_ids:
                self.participant_view.show_error_message("Nenhum evento selecionado.")
                return

            self._add_to_events(participant.id, selected_event_ids)

            self.participant_view.show_success_message("Participante adicionado aos eventos com sucesso!")
            
        except Exception as e:
            self._handle_error(e)

    def _get_participant_id(self):
        try:
            return int(self.participant_view.get_input("ID do participante: "))
        except ValueError:
            raise ValueError("ID inválido.")

    def _find_by_id(self):
        try:
            pid = self._get_participant_id()
            return self.participant_service.get_participant_by_id(pid)
        except Exception as e:
            self._handle_error(e)

    def _find_by_name(self):
        name = self.participant_view.get_input("Nome do participante: ").strip()
        results = self.participant_service.get_participants_by_name(name)
        
        if results:
            for participant in results:
                self.participant_view.show_participant(participant)
        else:
            self.participant_view.show_error_message("Nenhum participante encontrado com esse nome.")
            
    def _select_events_for_participant(self):
        events = self.event_service.get_all_events()
        if not events:
            self.participant_view.show_info_message("Nenhum evento disponível. Cadastre eventos primeiro.")
            return []
        
        self.participant_view.show_info_message("Selecione os eventos que o participante irá participar:")
        for event in events:
            self.participant_view.show_event(event)

        ids_input  = self.participant_view.get_input("IDs dos eventos (separados por vírgula): ")
        return [int(eid.strip()) for eid in ids_input.split(",") if eid.strip().isdigit()]
    
    def _add_to_events(self, participant_id, event_ids):
        for event_id in event_ids:
            self.event_service.add_participant_to_event(event_id, participant_id)
            
    def _handle_error(self, error):
        if isinstance(error, ParticipantValidationError):
            self.participant_view.show_error_message(str(error))
        elif isinstance(error, ValueError):
            self.participant_view.show_error_message("ID inválido.")
        else:
            self.participant_view.show_error_message(f"Erro inesperado: {str(error)}")
