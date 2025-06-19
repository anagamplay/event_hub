from controllers.event_controller import EventController
from controllers.participant_controller import ParticipantController
from views.menu_view import MenuView

class MenuController:
    def __init__(self):
        self.menu_view = MenuView()
        self.participant_controller = ParticipantController()
        self.event_controller = EventController()

    def show_main_menu(self):
        while True:
            main_menu_options = {
                '1': 'Participantes',
                '2': 'Eventos',
                '3': 'Relatórios',
                '0': 'Sair'
            }
            actions = {
                '1': self.show_participant_menu,
                '2': self.show_event_menu,
                '3': self.show_report_menu,
                '0': self.exit_program
            }

            choice = self.menu_view.show_menu("MENU PRINCIPAL", main_menu_options)
            action = actions.get(choice, self.invalid_option)
            action()

    def exit_program(self):
        self.menu_view.show_message("Saindo...")
        exit()

    def invalid_option(self):
        self.menu_view.show_message("Opção inválida.")

    def show_participant_menu(self):
        options = {
            '1': 'Cadastrar Participante',
            '2': 'Consultar Participante',
            '3': 'Atualizar Participante',
            '4': 'Remover Participante',
            '5': 'Listar Participantes',
            '0': 'Voltar'
        }

        choice = self.menu_view.show_menu("PARTICIPANTES", options)

        actions = {
            '1': lambda: print('Função ainda não implementada'),
            '2': lambda: print('Função ainda não implementada'),
            '3': lambda: print('Função ainda não implementada'),
            '4': lambda: print('Função ainda não implementada'),
            '5': lambda: print('Função ainda não implementada'),
            '0': self.show_main_menu
        }

        action = actions.get(choice, self.invalid_option)
        action()

    def show_event_menu(self):
        options = {
            '1': 'Cadastrar Evento',
            '2': 'Consultar Evento',
            '3': 'Atualizar Evento',
            '4': 'Remover Evento',
            '5': 'Listar Eventos',
            '0': 'Voltar'
        }

        choice = self.menu_view.show_menu("EVENTOS", options)

        actions = {
            '1': lambda: print('Função ainda não implementada'),
            '2': lambda: print('Função ainda não implementada'),
            '3': lambda: print('Função ainda não implementada'),
            '4': lambda: print('Função ainda não implementada'),
            '5': self.event_controller.list_events,
            '0': self.show_main_menu
        }

        action = actions.get(choice, self.invalid_option)
        action()

    def show_report_menu(self):
        options = {
            '1': 'Participantes mais ativos',
            '2': 'Eventos com poucos participantes',
            '3': 'Participantes únicos',
            '0': 'Voltar'
        }

        choice = self.menu_view.show_menu("RELATÓRIOS", options)

        actions = {
            '1': self.participant_controller.most_active_participants,
            '2': lambda: print('Função ainda não implementada'),
            '3': self.participant_controller.remove_duplicate_participants,
            '0': self.show_main_menu
        }

        action = actions.get(choice, self.invalid_option)
        action()

        #     participant = self.participant_controller.search_participant(
        #         participant_id)
        #     if participant:
        #         print(f"Participante encontrado:")
        #         print("Nome:", participant[0]['name'])
        #         print("Email:", participant[0]['email'])
        #     else:
        #         print("Participante não encontrado.")

        # elif choice == '2':
        #     participant_id = int(input("Digite o ID do participante: "))
        #     participant_events = self.participant_controller.participant_events(
        #         participant_id)
        #     for i, event in enumerate(participant_events):
        #         print(
        #             f"{i+1} | Nome: {event['name']} | Data: {event['date']} | Local: {event['location']}")

        # elif choice == '3':
        #     active_participants_ids = self.participant_controller.most_active_participants()
        #     print("Participantes mais ativos:")
        #     for participant_id in active_participants_ids:
        #         participant = self.participant_controller.search_participant(
        #             participant_id)
        #         if participant:
        #             print("Nome:", participant[0]['name'])
        #         else:
        #             print(
        #                 f"Participante com ID {participant_id} não encontrado.")

        # elif choice == '4':
        #     unique_participants = self.participant_controller.remove_duplicate_participants()
        #     print("Participantes sem duplicatas:")
        #     for participant in unique_participants:
        #         print(participant)

        # elif choice == '5':
        #     few_participants_events = self.participant_controller.events_with_few_participants()
        #     print("Eventos com poucos participantes:")
        #     for event in few_participants_events:
        #         print(
        #             f"ID: {event['id']} | Nome: {event['name']} | Data: {event['date']} | Local: {event['location']}")

        # elif choice == '6':
        #     print("\neventos disponíveis:")
        #     self.event_controller.list_events()

        # elif choice == '7':
        #     print("Lista de Participantes:")
        #     self.participant_controller.list_participants()

        # elif choice == '8':
        #     name = input("Digite o nome do participante: ")
        #     email = input("Digite o email do participante: ")
        #     new_participant = {
        #         'name': name,
        #         'email': email
        #     }
        #     self.participant_controller.add_participant(new_participant)
        #     print(f"Participante {name} cadastrado com sucesso!")

        # elif choice == '9':
        #     name = input("Digite o nome do evento: ")
        #     date = input("Digite a data do evento (DD/MM/AAAA): ")
        #     location = input("Digite o local do evento: ")
        #     new_event = {
        #         'name': name,
        #         'date': date,
        #         'location': location,
        #         'participants': []
        #     }
        #     self.event_controller.add_event(new_event)
        #     print(f"Evento {name} cadastrado com sucesso!")

        # elif choice == '0':
        #     print("Saindo do sistema. Até logo!")
        #     break

        # else:
        #     print("Opção inválida. Tente novamente.")
