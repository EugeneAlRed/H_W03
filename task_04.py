import datetime
from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """need to congratulate

    Args:
        users (list(dict)): username and birthday

    Returns:
        list(dict): need to congratulate
    """
    date_now = datetime.today().date()
    birthday = []
    for user in users:
        birthday_date = user['birthday']
        birthday_date = str(date_now.year) + birthday_date[4:]
        birthday_date = datetime.strptime(birthday_date, '%Y.%m.%d').date()
        day_difference = (birthday_date - date_now).days
        day_week = birthday_date.isoweekday()
        if day_difference >= 0 and day_difference < 7:
            if day_week < 6:
                birthday.append(
                    {'name': user['name'], 'birthday': birthday_date.strftime('%Y.%m.%d')})
            else:
                if (birthday_date + timedelta(day=2)).weekday() == 0:
                    birthday.append({'name': user['name'], 'birthday': (
                        birthday_date + timedelta(day=2)).strftime('%Y.%m.%d')})
                elif (birthday_date + timedelta(day=1)).weekday() == 0:
                    birthday.append({'name': user['name'], 'birthday': (
                        birthday_date + timedelta(day=1)).strftime('%Y.%m.%d')})
    return birthday


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.26"},
    {"name": "Jane ", "birthday": "1990.01.31"}
]

print(get_upcoming_birthdays(users))