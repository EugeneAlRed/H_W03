import re


def normalize_phone(phone_number):
    """normalizes phone numbers to a standard format

    Args:
        phone_number (str): line with a phone number

    Returns:
        str: normalized phone number
    """
    pattern = r'\+?\d+'
    matches = re.findall(pattern, phone_number)
    matches = ''.join(matches)
    if matches.startswith('380'):
        matches = '+' + matches
    elif not matches.startswith('+380'):
        matches = '+38' + matches
    return matches


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
