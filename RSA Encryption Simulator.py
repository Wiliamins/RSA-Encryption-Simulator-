import random
import math

# Funkcja do sprawdzania, czy liczba jest pierwsza
def czy_pierwsza(n, k=5):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 1)
        if math.gcd(a, n) != 1:
            return False
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Funkcja do generowania kluczy RSA
def generuj_klucze(bit_length=1024):
    # Wybieranie dwóch dużych liczb pierwszych
    p = random.getrandbits(bit_length)
    while not czy_pierwsza(p):
        p = random.getrandbits(bit_length)

    q = random.getrandbits(bit_length)
    while not czy_pierwsza(q) or q == p:
        q = random.getrandbits(bit_length)

    # Obliczanie N
    N = p * q

    # Obliczanie funkcji Eulera
    euler = (p - 1) * (q - 1)

    # Wybieranie liczby e względnie pierwszej z eulerem
    e = random.randrange(2, euler)
    while math.gcd(e, euler) != 1:
        e = random.randrange(2, euler)

    # Obliczanie odwrotności modulo e w stosunku do euler
    d = pow(e, -1, euler)

    return ((N, e), (N, d))

# Funkcja do szyfrowania wiadomości
def zaszyfruj(tekst, klucz):
    N, e = klucz
    zaszyfrowane = [pow(ord(znak), e, N) for znak in tekst]
    return zaszyfrowane

# Funkcja do odszyfrowywania wiadomości
def odszyfruj(zaszyfrowane, klucz):
    N, d = klucz
    odszyfrowane = [chr(pow(znak, d, N)) for znak in zaszyfrowane]
    return ''.join(odszyfrowane)

# Funkcja do wprowadzania wiadomości przez użytkownika
def wprowadz_wiadomosc():
    wiadomosc = input("Wprowadź wiadomość do zaszyfrowania: ")
    return wiadomosc

# Przykładowe użycie
if __name__ == "__main__":
    # Generowanie kluczy
    klucz_publiczny, klucz_prywatny = generuj_klucze()

    # Wprowadzanie wiadomości przez użytkownika
    wiadomosc = wprowadz_wiadomosc()

    # Szyfrowanie
    zaszyfrowane = zaszyfruj(wiadomosc, klucz_publiczny)
    print("Zaszyfrowana wiadomość:", zaszyfrowane)

    # Odszyfrowywanie
    odszyfrowane = odszyfruj(zaszyfrowane, klucz_prywatny)
    print("Odszyfrowana wiadomość:", odszyfrowane)
