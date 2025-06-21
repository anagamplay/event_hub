import re
from core.exceptions.event_validation_error import EventValidationError
from core.validators.form_validator import FormValidator

class EventValidator:
    def validate(self, name: str, description: str, date: str, location: str):
        name = FormValidator.normalize(name)
        description = FormValidator.normalize(description)
        date = FormValidator.normalize(date)
        location = FormValidator.normalize(location)

        FormValidator.validate_required(name, "nome")
        FormValidator.validate_only_letters(name, "nome")
        
        FormValidator.validate_required(description, "descrição")

        FormValidator.validate_required(date, "data")
        self.validate_date_format(date)

        FormValidator.validate_required(location, "local")

    def validate_date_format(self, date_str: str):
        pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        if not re.fullmatch(pattern, date_str):
            raise EventValidationError("A data deve estar no formato DD/MM/AAAA.")
