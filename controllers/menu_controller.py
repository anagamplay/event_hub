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

    def show_participant_menu(self):
        options = {
            '1': 'Cadastrar Participante',
            '2': 'Consultar Participante',
            '3': 'Atualizar Participante',
            '4': 'Remover Participante',
            '5': 'Listar Participantes',
            '6': 'Adicionar Participante a um Evento',
            '0': 'Voltar'
        }
        choice = self.menu_view.show_menu("PARTICIPANTES", options)
        actions = {
            '1': self.participant_controller.add_participant,
            '2': self.participant_controller.find_participant,
            '3': self.participant_controller.update_participant,
            '4': self.participant_controller.remove_participant,
            '5': self.participant_controller.list_participants,
            '6': self.participant_controller.add_participant_to_event,
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
            '1': self.event_controller.add_event,
            '2': self.event_controller.find_event,
            '3': self.event_controller.update_event,
            '4': self.event_controller.remove_event,
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
            '2': self.event_controller.list_events_with_few_participants,
            '3': self.participant_controller.remove_duplicate_participants,
            '0': self.show_main_menu
        }
        action = actions.get(choice, self.invalid_option)
        action()

    def exit_program(self):
        self.menu_view.show_message("Saindo...")
        exit()

    def invalid_option(self):
        self.menu_view.show_message("Opção inválida.")
