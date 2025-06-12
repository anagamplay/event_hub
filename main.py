from events.events_service import EventService
from participants.participants_service import ParticipantsService
from menu.menu_service import Menu


def main():
    print("Bem-vindo ao sistema de gerenciamento de events!")

    Menu.show()
    
    while True:
        choice = Menu.get_user_choice()

        if choice == '1':
            participant_id = int(input("Digite o ID do participante: "))
            participant = ParticipantsService.search_participant(participant_id)
            if participant:
                print(f"Participante encontrado:")
                print("Nome:", participant[0]['name'])
                print("Email:", participant[0]['email'])
            else:
                print("Participante não encontrado.")

        elif choice == '2':
            participant_id = int(input("Digite o ID do participante: "))
            participant_events = ParticipantsService.participant_events(participant_id)
            for i, event in enumerate(participant_events):
                print(f"{i+1} | Nome: {event['name']} | Data: {event['date']} | Local: {event['location']}")

        elif choice == '3':
            active_participants = ParticipantsService.most_active_participants()
            print("Participantes mais ativos:")
            for participant in active_participants:
                print(participant)

        elif choice == '4':
            unique_participants = ParticipantsService.remove_duplicate_participants()
            print("Participantes sem duplicatas:")
            for participant in unique_participants:
                print(participant)

        elif choice == '5':
            few_participants_events = ParticipantsService.events_with_few_participants()
            print("Eventos com poucos participantes:")
            for event in few_participants_events:
                print(event)

        elif choice == '6':
            EventService.list_events()

        elif choice == '0':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
