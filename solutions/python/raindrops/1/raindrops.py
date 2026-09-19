def convert(number):
    resultat = ""
    
    if number % 3 == 0:
        resultat += "Pling"
    if number % 5 == 0:
        resultat += "Plang"
    if number % 7 == 0:
        resultat += "Plong"

    return resultat or str(number)
