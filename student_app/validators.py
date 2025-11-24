import re
from django.core.exceptions import ValidationError


def validate_name_format(value: str):
    full_name = re.compile(r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$')
    if not full_name.match(value):
        raise ValidationError(
            'Name must be in the format "First Middle Initial. Last"'
        )


def validate_school_email(value: str):
    email_pattern = re.compile(r'^.+@school\.com$')
    if not email_pattern.match(value):
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')


def validate_combination_format(value: str):
    combo_format = re.compile(r'^\d{2}-\d{2}-\d{2}$')
    if not combo_format.match(value):
        raise ValidationError(
            'Combination must be in the format "12-12-12"'
        )
