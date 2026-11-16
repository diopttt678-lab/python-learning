def is_armstrong_number(number):
    number_str=str(number)
    expo=len(number_str)
    total=sum(int(c)**expo for c in number_str)
    if total == int(number_str):
        return True
    return False
