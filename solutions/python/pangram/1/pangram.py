def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence_lower = sentence.lower()
    
    for letter in alphabet:
        if letter not in sentence_lower:
            return False  
            
    return True  