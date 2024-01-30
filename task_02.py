import random


def get_numbers_ticket(min, max, quantity):
    """
    Get numbers ticket

    Args:
        min (int): minimum possible number in a set
        max (int): maximum possible number for a set
        quantity (int): The number of numbers that need to be selected (values ​​between min and max). 

    Returns:
        list: list of randomly selected, sorted numbers.
    """
    lottery_numbers = []
    while quantity > len(lottery_numbers):
        lottery_numbers = list(lottery_numbers)
        lottery_numbers.append(random.randint(min, max))
        lottery_numbers = set(lottery_numbers)
    return list(lottery_numbers)



