from core.validators.form_validator import FormValidator

class ParticipantValidator:
    @staticmethod
    def validate(name: str, email: str):
        name = FormValidator.normalize(name)
        email = FormValidator.normalize(email)

        FormValidator.validate_required(name, "nome")
        FormValidator.validate_only_letters(name, "nome")

        FormValidator.validate_required(email, "email")
        FormValidator.validate_email(email)