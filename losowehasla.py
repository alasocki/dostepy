"""
Generator losowych haseł spełniających następujące wymagania:
min. 8 znaków (nakładam dodatkowo górne ograniczenie 24 znaki)
wielkie i małe litery
cyfry
znaki specjalne
bez słów encyklopedycznych
"""

import random
import string


def losowehasla():

    lista_znakow = tuple(string.ascii_letters + string.digits + "!@#$%^&(){}[]")

    haselko = []

    for _ in range(random.randint(8,24)):
        haselko.append(random.choice(lista_znakow))

    print(''.join(haselko))
    return ''.join(haselko)


losowehasla()
