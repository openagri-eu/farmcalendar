import re
from datetime import datetime

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


def validate_datetime_format(value):
    """Validate datetime field to accept multiple date and time formats."""

    # If value is already a datetime object, no need to validate format
    if isinstance(value, datetime):
        return

    # List of accepted datetime formats
    datetime_formats = [
        '%Y-%m-%d %H:%M:%S',  # yyyy-mm-dd hh:mm:ss
        '%Y-%m-%d',           # yyyy-mm-dd
        '%d-%m-%Y',           # dd-mm-yyyy
        '%d-%m-%Y %H:%M:%S'   # dd-mm-yyyy hh:mm:ss
    ]

    # Attempt to parse the value with each format
    for fmt in datetime_formats:
        try:
            datetime.strptime(value, fmt)  # This will raise a ValueError if format does not match
            return  # If parsing succeeds, the format is valid
        except ValueError:
            continue  # Try the next format

    # If none of the formats match, raise a ValidationError
    raise ValidationError(
        "Date and time format must be one of the following: yyyy-mm-dd hh:mm:ss, yyyy-mm-dd, dd-mm-yyyy, "
        "or dd-mm-yyyy HH:mm:ss."
    )


def validate_coordinates(value):
    """Validate coordinates in the format latitude,longitude (e.g., '40.7128,-74.0060')."""
    coordinate_pattern = r'^-?\d{1,3}\.\d+,-?\d{1,3}\.\d+$'
    if not re.match(coordinate_pattern, value):
        raise ValidationError(
            "Coordinates must be in the format 'latitude,longitude' (e.g., '40.7128,-74.0060')."
        )


def validate_positive(value):
    """Ensure the value is positive."""
    if value < 0:
        raise ValidationError("This field must be a positive number.")


