from views.menu_view import MenuView

class MenuController:
    def start(self):
        MenuView.show()

        while True:
            choice = MenuView.get_user_choice()

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
                active_participants_ids = ParticipantsService.most_active_participants()
                print("Participantes mais ativos:")
                for participant_id in active_participants_ids:
                    participant = ParticipantsService.search_participant(participant_id)
                    if participant:
                        print("Nome:", participant[0]['name'])
                    else:
                        print(f"Participante com ID {participant_id} não encontrado.")

            elif choice == '4':
                unique_participants = ParticipantsService.remove_duplicate_participants()
                print("Participantes sem duplicatas:")
                for participant in unique_participants:
                    print(participant)

            elif choice == '5':
                few_participants_events = ParticipantsService.events_with_few_participants()
                print("Eventos com poucos participantes:")
                for event in few_participants_events:
                    print(f"ID: {event['id']} | Nome: {event['name']} | Data: {event['date']} | Local: {event['location']}")

            elif choice == '6':
                print("\neventos disponíveis:")
                EventService.list_events()
                
            elif choice == '7':
                print("Lista de Participantes:")
                ParticipantsService.list_participants()
                
            elif choice == '8':
                name = input("Digite o nome do participante: ")
                email = input("Digite o email do participante: ")
                new_participant = {
                    'name': name,
                    'email': email
                }
                ParticipantsService.add_participant(new_participant)
                print(f"Participante {name} cadastrado com sucesso!")
                
            elif choice == '9':
                name = input("Digite o nome do evento: ")
                date = input("Digite a data do evento (DD/MM/AAAA): ")
                location = input("Digite o local do evento: ")
                new_event = {
                    'name': name,
                    'date': date,
                    'location': location,
                    'participants': []
                }
                EventService.add_event(new_event)
                print(f"Evento {name} cadastrado com sucesso!")

            elif choice == '0':
                print("Saindo do sistema. Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")