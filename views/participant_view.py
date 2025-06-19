from models.participant_model import Participant

class ParticipantView:
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