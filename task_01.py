from datetime import datetime


def get_days_from_today(date):
    """calculates the number of days between the given date and the current date.

    Args:
        date (str): a string representing a date

    Returns:
        int: integer
    """
    try:
        other_date = datetime.strptime(date, '%Y-%m-%d')
        date_now = datetime.today()
        number_days = date_now.toordinal() - other_date.toordinal()
        return number_days
    except ValueError:
        print("That was no valid date. Try again, for example: '2020-10-24'")



