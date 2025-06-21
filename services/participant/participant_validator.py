from core.exceptions.validation_error import ParticipantValidationError
from core.validators.form_validator import FormValidator

class ParticipantValidator:
    def __init__(self, participant_list):
        self.participant_list = participant_list
        
    @staticmethod
    def validate(name: str, email: str):
        name = FormValidator.normalize(name)
        email = FormValidator.normalize(email)

        FormValidator.validate_required(name, "nome")
        FormValidator.validate_only_letters(name, "nome")

        FormValidator.validate_required(email, "email")
        FormValidator.validate_email(email)
        
    def validate_email_not_in_use(self, email: str):
        for participant in self.participant_list:
            if participant['email'].lower() == email.lower():
                raise ParticipantValidationError("O e-mail informado já está cadastrado.")