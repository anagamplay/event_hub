class EventView:
    @staticmethod
    def show_title(title: str):
        print("\n" + "=" * (len(title) + 10))
        print(f"     {title}     ")
        print("=" * (len(title) + 10))

    @staticmethod
    def get_input(prompt: str) -> str:
        return input(f"{prompt}: ")

    @staticmethod
    def show_success_message(message: str):
        print(f"\n✅ {message}\n")

    @staticmethod
    def show_error_message(message: str):
        print(f"\n❌ {message}\n")

    def show_info_message(self, message):
        print(f"{message}")

    def show_event(self, event):
        print(
            f"ID: {event.id} | Nome: {event.name} | Data: {event.date} | Local: {event.location}")
