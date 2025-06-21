import re
from core.exceptions.validation_error import ParticipantValidationError

class FormValidator:
    @staticmethod
    def normalize(value: str) -> str:
        return value.strip() if isinstance(value, str) else ""

    @staticmethod
    def validate_required(field: str, field_name: str):
        if not field:
            raise ParticipantValidationError(f"O campo '{field_name}' não pode ser vazio.")

    @staticmethod
    def validate_only_letters(field: str, field_name: str):
        if not re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", field):
            raise ParticipantValidationError(f"O campo '{field_name}' deve conter apenas letras e espaços.")

    @staticmethod
    def validate_email(field: str):
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.fullmatch(email_pattern, field):
            raise ParticipantValidationError("Formato de email inválido.")
