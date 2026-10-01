"""Validation rules for manuscript records.

YOU IMPLEMENT THIS FILE.

Every validate_* function takes a raw string (exactly as it came out of the
CSV file) and returns a tuple:

    (True, "")              the value is trustworthy
    (False, "reason here")  the value is not, and here is why

The reason is a short human-readable string. The autograder checks the
boolean, not your exact wording — but a teammate reading your rejection log
should understand it, so write it for them.

READ THIS BEFORE YOU START
--------------------------
The year range is INCLUSIVE at both ends: 1100 and 1900 are VALID.
1099 and 1901 are not. Most marks lost in Part A are lost on that line.
"""

from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["Timbuktu", "Djenne", "Gao", "Walata", "Chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 1100
MAX_YEAR = 1900

def validate_id(value):
    if not isinstance(value, str) or len(value) != 5:
        return (False, "not in range")
    if value.startswith("MS") and value[2:].isdigit():
        return (True, "")
    else:
        return (False, "not valid")


def validate_title(value):
    """A title must be present and at least 3 characters once stripped.

    Valid:   "Tarikh al-Sudan"
    Invalid: "", "   ", "Ab"

    Returns (bool, str).
    """
    raise NotImplementedError("validate_title")


def validate_city(value):
    """A city must be present and appear in KNOWN_CITIES.

    Comparison is case-insensitive: "timbuktu" is acceptable.
    "Kano" is not in our list, so it is rejected — and that is a real
    decision with a cost. Write about it in your README.

    Returns (bool, str).
    """
    raise NotImplementedError("validate_city")

def validate_year(value):
    if not isinstance(value, str) or len(value) != 4 or not value.isdigit():
        if isinstance(value, str) and not value.isdigit():
            return (False, "year should be integers")
        return (False, "invalid year")
    year = int(value)
    if 1100 <= year <= 1900:
        return (True, "")
    else:
        return (False, "not in range")


def validate_condition(value):
    if not isinstance(value, str):
        return (False, "a condition is either fragile, good or fair")
        
    valid_conditions = ("fragile", "good", "fair")
    
    if value.lower() in valid_conditions:
        return (True, "")
    else:
        return (False, "a condition is either fragile, good or fair")



def validate_record(record):
    """Validate a whole record dictionary.

    record is a dict with the keys: id, title, city, year, condition.

    Returns a LIST of reasons the record is invalid — one string per broken
    rule, in this field order: id, title, city, year, condition.
    An empty list means the record is valid.

    Do not re-write the rules here. Call the five functions above.
    """
    raise NotImplementedError("validate_record")
