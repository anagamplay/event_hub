from core.exceptions.event_validation_error import EventValidationError
from models.event_model import Event
from services.event.event_service import EventService
from services.participant.participant_service import ParticipantService
from views.event_view import EventView

class EventController:
    def __init__(self):
        self.event_service = EventService()
        self.event_view = EventView()
        self.participant_service = ParticipantService()

    def add_event(self):
        self.event_view.show_title("Cadastro de Evento")
        try:
            name = self.event_view.get_input("Nome do evento: ")
            description = self.event_view.get_input("Descrição do evento: ")
            date = self.event_view.get_input("Data (DD/MM/AAAA): ")
            location = self.event_view.get_input("Local: ")

            new_event = self.event_service.create_event(name, description, date, location)
            self.event_view.show_success_message("Evento cadastrado com sucesso!")
            self.event_view.show_event(new_event)

        except EventValidationError as ve:
            self.event_view.show_error_message(str(ve))
        except Exception as e:
            self.event_view.show_error_message(f"Erro inesperado: {str(e)}")

    def list_events(self):
        self.event_view.show_title("Lista de Eventos")
        events = self.event_service.get_all_events()

        for event in events:
            self.event_view.show_event(event)

    def find_event(self):
        self.event_view.show_title("Consultar Evento")
        try:
            event_id = int(self.event_view.get_input("ID do evento: "))
            event = self.event_service.get_event_by_id(event_id)
            if event:
                self.event_view.show_event(event)
                
                if not event.participants:
                    self.event_view.show_info_message("  Nenhum participante inscrito.")
                else:
                    self.event_view.show_info_message("  Participantes:")
                    for participant_id in event.participants:
                        participant = self.participant_service.get_participant_by_id(participant_id)
                        if participant:
                            self.event_view.show_info_message(f"    - {participant.name} ({participant.email})")
            else:
                self.event_view.show_error_message("Evento não encontrado.")
        except ValueError:
            self.event_view.show_error_message("ID inválido.")

    def update_event(self):
        self.event_view.show_title("Atualizar Evento")
        try:
            event_id = int(self.event_view.get_input("ID do evento: "))
            event = self.event_service.get_event_by_id(event_id)
            if not event:
                self.event_view.show_error_message("Evento não encontrado.")
                return

            self.event_view.show_event(event)
            self.event_view.show_info_message("Deixe em branco para manter os dados atuais.")

            name = self.event_view.get_input("Novo nome: ").strip()
            description = self.event_view.get_input("Nova descrição: ").strip()
            date = self.event_view.get_input("Nova data (DD/MM/AAAA): ").strip()
            location = self.event_view.get_input("Novo local: ").strip()

            updated_event = self.event_service.update_event(
                event_id,
                name=name or event.name,
                description=description or event.description, 
                date=date or event.date,
                location=location or event.location
            )

            self.event_view.show_success_message("Evento atualizado com sucesso!")
            self.event_view.show_event(updated_event)

        except EventValidationError as ve:
            self.event_view.show_error_message(str(ve))
        except ValueError:
            self.event_view.show_error_message("ID inválido.")
        except Exception as e:
            self.event_view.show_error_message(f"Erro inesperado: {str(e)}")

    def remove_event(self):
        self.event_view.show_title("Remover Evento")
        try:
            event_id = int(self.event_view.get_input("ID do evento: "))
            event = self.event_service.get_event_by_id(event_id)
            if not event:
                self.event_view.show_error_message("Evento não encontrado.")
                return
            
            if event.participants:  # <- Verifica se há participantes
                self.event_view.show_error_message("Não é possível remover um evento com participantes cadastrados.")
                return

            confirm = self.event_view.get_input(
                f"Tem certeza que deseja remover o evento '{event.name}'? (s/n): "
            ).strip().lower()

            if confirm == 's':
                self.event_service.remove_event(event_id)
                self.event_view.show_success_message("Evento removido com sucesso.")
            else:
                self.event_view.show_info_message("Remoção cancelada.")
        except ValueError:
            self.event_view.show_error_message("ID inválido.")
        except Exception as e:
            self.event_view.show_error_message(f"Erro inesperado: {str(e)}")
            
    def list_events_with_few_participants(self):
        self.event_view.show_title("Eventos com Poucos Participantes")
        events = self.event_service.get_events_with_few_participants()
        if events:
            for event in events:
                self.event_view.show_event(event)
        else:
            self.event_view.show_info_message("Nenhum evento com poucos participantes encontrado.")


