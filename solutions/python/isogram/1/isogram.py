def is_isogram(phrase):
    phrases=phrase.replace("-", "").replace(" ","").lower()
    for letter in phrases:
        if phrases.count(letter) != 1:
            return False
    return True