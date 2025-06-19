from controllers.menu_controller import MenuController

def main():
    print("Bem-vindo ao sistema de gerenciamento de eventos!")
    menu_controller = MenuController()
    menu_controller.show_main_menu()

if __name__ == "__main__":
    main()
