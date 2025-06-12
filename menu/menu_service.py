class Menu:
  def show():
    print("======== MENU ========")
    print("1. Consultar Participante")
    print("2. Mostrar Eventos do Participante")
    print("3. Mostrar Participantes Mais Ativos")
    print("4. Remover Participantes Duplicados")
    print("5. Mostrar Eventos com Poucos Participantes")
    print("6. Listar Eventos")
    print("0. Sair")

  def get_user_choice():
      choice = input("Escolha uma opção: ")
      return choice