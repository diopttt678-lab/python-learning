def is_armstrong_number(number):
    number=str(number)
    len_number = len(number)
    total = sum(int(c) ** len_number for c in number)
    total == int(number)
    if total == int(number):
        return True
    return False
    pass
