def response(hey_bob):
    text = hey_bob.strip()

    if not text:
        return "Fine. Be that way!"

    is_yelling = text.isupper()
    is_question = text.endswith("?")

    if is_yelling:
        return "Calm down, I know what I'm doing!" if is_question else "Whoa, chill out!"
    if is_question:
        return "Sure."
    
    return "Whatever."