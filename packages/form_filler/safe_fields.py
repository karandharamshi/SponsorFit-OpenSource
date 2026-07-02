SAFE_FIELD_HINTS = {
    "first_name": ["first name", "firstname", "given name"],
    "last_name": ["last name", "lastname", "surname", "family name"],
    "email": ["email", "e-mail"],
    "phone": ["phone", "mobile", "telephone"],
    "city": ["city", "town"],
    "country": ["country"],
}

SENSITIVE_HINTS = [
    "submit",
    "send application",
    "declaration",
    "right to work",
    "visa",
    "sponsorship",
    "disability",
    "ethnicity",
    "gender",
    "religion",
    "criminal",
    "conviction",
    "medical",
    "reasonable adjustment",
    "equality",
    "equal opportunities",
]


def is_sensitive_field(label: str) -> bool:
    return any(hint in label.lower() for hint in SENSITIVE_HINTS)
