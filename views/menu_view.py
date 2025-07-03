class MenuView:
    @staticmethod
    def show_menu(title: str, options: dict):
        print("\n" + "=" * (len(title) + 10))
        print(f"     {title}     ")
        print("=" * (len(title) + 10))
        for key, value in options.items():
            print(f"{key}. {value}")
        return input("Escolha uma opção: ")

    @staticmethod
    def show_message(message: str):
        print(f"\n{message}")
