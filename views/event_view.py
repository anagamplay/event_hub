class EventView:
    @staticmethod
    def show_title(title: str):
        print(f"\n---- {title} ----")
    
    @staticmethod
    def get_input(prompt: str) -> str:
        return input(f"{prompt}")

    @staticmethod
    def show_success_message(message: str):
        print(f"\n{message}")
        
    @staticmethod
    def show_error_message(message: str):
        print(f"\n[ERROR] {message}")
        
    def show_info_message(self, message):
        print(f"[INFO] {message}")
        
    def show_event(self, event):
        print(str(event))