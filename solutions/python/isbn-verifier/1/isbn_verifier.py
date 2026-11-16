def is_valid(isbn):
    simple_isbn = isbn.replace("-", "")

    if (
        len(simple_isbn) != 10
        or not simple_isbn[:9].isdigit()
        or not (simple_isbn[-1].isdigit() or simple_isbn[-1].upper() == "X")
    ):
        return False

    total = sum(
        (10 if carac.upper() == "X" and i == 9 else int(carac)) * (10 - i)
        for i, carac in enumerate(simple_isbn)
    )

    return total % 11 == 0
