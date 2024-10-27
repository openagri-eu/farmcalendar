from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_name_field(value):
    """Validate fields to allow letters, numbers, spaces, and certain symbols."""
    name_pattern = r'^[a-zA-Z0-9.,_()\[\]{}\-\*\&\@\:\;\ ]+$'
    name_validator = RegexValidator(
        regex=name_pattern,
        message="This field must contain only letters, numbers, spaces, and . , _ - () [] {} ; : & @ *",
        code='invalid_name'
    )
    name_validator(value)  # Raises ValidationError if invalid

    # Additional check to disallow the default "Unnamed" value
    if value == "Unnamed":
        raise ValidationError("The field cannot be 'Unnamed'. Please provide a valid name.")


def validate_phone_number(value):
    """Validate phone number format, allowing + and - and requiring 9-15 digits."""
    phone_pattern = r'^\+?[0-9\-]{9,15}$'
    phone_validator = RegexValidator(
        regex=phone_pattern,
        message="The phone number must be between 9 to 15 digits, starting with + if needed, and may contain - signs.",
        code='invalid_phone'
    )
    phone_validator(value)  # Raises ValidationError if invalid


def validate_vat_id(value):
    """Ensure VAT ID contains only alphanumeric characters."""
    if not value.isalnum():
        raise ValidationError("The VAT ID should contain only alphanumeric characters.")

