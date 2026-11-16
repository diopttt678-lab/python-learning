def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    # Calcule la somme des grains sur les 64 cases
    return sum(2 ** i for i in range(64))
