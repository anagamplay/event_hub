class MenuView:
    @staticmethod
    def show_menu(title: str, options: dict):
        print(f"\n---- {title} ----")
        for key, value in options.items():
            print(f"{key}. {value}")
        return input("Escolha uma opção: ")

    @staticmethod
    def show_message(message: str):
        print(f"\n{message}")
