"""
Funkcja szyfrująca podany tekst do formatu base64.
"""

import base64


def szyfrowanieb64(tekst='Kot'):

    utajniony_tekst = base64.b64encode(tekst.encode())
    return utajniony_tekst


a = szyfrowanieb64('Bla Bla Bla, HaHaha! :)')
print(a)

def deszyfrowanieb64(a):

    odtajniony_tekst = base64.b64decode(a)
    return odtajniony_tekst.decode()


b = deszyfrowanieb64(a)
print(b)