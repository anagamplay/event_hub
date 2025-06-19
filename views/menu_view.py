class MenuView:
  @staticmethod
  def show():
    print("======== MENU ========")
    print("1. Consultar Participante")
    print("2. Mostrar Eventos do Participante")
    print("3. Mostrar Participantes Mais Ativos")
    print("4. Remover Participantes Duplicados")
    print("5. Mostrar Eventos com Poucos Participantes")
    print("6. Listar Eventos")
    print("7. Listar Participantes")
    print("8. Cadastrar Participante")
    print("9. Cadastrar Evento")
    print("0. Sair")
    
  @staticmethod
  def get_user_choice():
      choice = input("Escolha uma opção: ")
      return choice