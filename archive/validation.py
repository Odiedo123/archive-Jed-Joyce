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

#from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["Timbuktu", "Djenne", "Gao", "Walata", "Chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 1100
MAX_YEAR = 1900

def validate_id(value):
    """An ID is the letters 'MS' followed by exactly three digits.

    Valid:   "MS001", "MS742"
    Invalid: "MS1", "MS0012", "ms001", "XX001", "", "MS00A"

    Returns (bool, str).
    """
    raise NotImplementedError("validate_id")
    if not isinstance(value, str) or len(value) != 5:
        return (False, "not in range")
    if value.startswith("MS") and value[2:].isdigit():
        return (True, "")
    else:
        return (False, "not valid")


def validate_title(value):
    value = value.strip()
    statement = True
    s = ""
    if len(value) < 3:
        s = "A title must be present and at least 3 characters once stripped"
        statement = False

    return statement,s
    raise NotImplementedError("validate_title")


def validate_city(value):
    s = ''
    statement = True
    KNOWN_CITIES2 = []
    for i in range(0,len(KNOWN_CITIES)):
        KNOWN_CITIES2.append(KNOWN_CITIES[i].lower());
    if value.lower() not in KNOWN_CITIES2:
        s = value + " " + "is not in our list, so it is rejected"
        statement = False;
    return statement,s
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
    if value.lower() in VALID_CONDITIONS:
        return (True, "")
    else:
        return (False, "a condition is either fragile, good or fair")



def validate_record(record):
    issues = []
    if validate_id(record["id"])[0] == False:
        issues.append(validate_id(record["id"])[1])
    if validate_title(record["title"])[0] == False:
        issues.append(validate_title(record["title"])[1])
    if validate_city(record("city"))[0] == False:
        issues.append(validate_city(record["city"])[1])
    if validate_year(record["year"])[0] == False:
        issues.append(validate_year(record["year"])[1])
    if validate_condition(record["condition"])[0] == False:
        issues.append(validate_condition(record["condition"])[1])

    return issues
    raise NotImplementedError("validate_record")