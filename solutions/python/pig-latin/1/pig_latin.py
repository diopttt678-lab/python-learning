def translate(TEXT):
    words = TEXT.split()
    return " ".join(translate_word(word) for word in words)


def translate_word(word):
    vowels = "aeiou"

    if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
        return word + "ay"

    for i, letter in enumerate(word):
        if letter == "q" and i + 1 < len(word) and word[i + 1] == "u":
            split = i + 2
            return word[split:] + word[:split] + "ay"
        if letter in vowels:
            return word[i:] + word[:i] + "ay"
        if letter == "y" and i > 0:
            return word[i:] + word[:i] + "ay"

    return word + "ay"