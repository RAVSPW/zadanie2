

def gcd(a, b):
    # Zwróć GCD a i b za pomocą algorytm Euklidesa
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Zwraca modularną odwrotność % m
    # czyli liczbę x taką, że a * x% m = 1

    if gcd(a, m) != 1:
        return None # brak odwrotności mod, jeśli a & m nie są względnie pierwsze

    # Oblicz za pomocą rozszerzonego algorytmu euklidesowego:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // jest operatorem dzielenia liczby całkowitej
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m