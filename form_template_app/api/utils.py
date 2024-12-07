import re
from datetime import datetime


def determine_field_type(value):
    """Валидация полей."""
    if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
        return 'phone'
    try:
        datetime.strptime(value, '%d.%m.%Y')
        return 'date'
    except ValueError:
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return 'date'
        except ValueError:
            pass
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
        return 'email'
    return 'text'
