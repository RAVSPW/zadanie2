
import random, sys, os, Euklides, cryptomath


def main():
    # utwórz parę kluczy publiczny / prywatny z kluczami z ustalonymi rozmiarami
    print('Tworzenie plików z kluczami...')
    makeKeyFiles('plik',  512)
    print('Utworzono pliki z kluczami.')

def generateKey(keySize):
    # Tworzy parę kluczy publiczny / prywatny z kluczami o rozmiarze keySize
    #  Uruchomienie tej funkcji może chwilę potrwać.

    # Step 1: Utwórz dwie liczby pierwsze, p i q. Oblicz n = p * q.
    print('Generowanie liczby pierwszej p...')
    p = Euklides.generateLargePrime(keySize)
    print('Generowanie liczby pierwszej q...')
    q = Euklides.generateLargePrime(keySize)
    n = p * q

    # Step 2: Utwórz liczbę e, która jest względnie pierwsza do (p-1) * (q-1)
    print('Generowanie e, które jest względnie pierwsze dla (p-1) * (q-1)...')
    while True:
        # Wypróbuj losowe liczby dla e, aż jedna będzie ważna.
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Oblicz d, odwrotność mod e.
    print('Obliczanie d, czyli mod odwrotności e...')
    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Klucz publiczny:', publicKey)
    print('Klucz prywatny:', privateKey)

    return (publicKey, privateKey)


def makeKeyFiles(name, keySize):
    # Tworzy dwa pliki „x_publickey.txt” i „x_privatekey.txt” (gdzie x jest wartością w nazwie)
    # z zapisanymi w nich liczbami całkowitymi n, e i d, e,
    # oddzielonymi przecinkami.

    # Nasza kontrola bezpieczeństwa uniemożliwi nam nadpisanie naszych starych plików kluczy:
    if os.path.exists('%s_publickey.txt' % (name)) or os.path.exists('%s_privatekey.txt' % (name)):
        sys.exit('OSTRZEŻENIE: plik% s_publickey.txt lub% s_privatekey.txt już istnieje! Użyj innej nazwy lub usuń te pliki i ponownie uruchom ten program.' % (name, name))

    publicKey, privateKey = generateKey(keySize)

    print()
    print('Klucz publiczny to %s i %s cyfr.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Zapisywanie klucza publicznego do pliku %s_publickey.txt...' % (name))
    fo = open('%s_publickey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    print()
    print('Klucz prywatny to %s i %s cyfr.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Zapis klucza prywatnego do pliku %s_privatekey.txt...' % (name))
    fo = open('%s_privatekey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()


# Jeśli makeRsaKeys.py jest uruchomiony (zamiast importowanego jako moduł), wywołaj funkcję main ().
if __name__ == '__main__':
    main()

