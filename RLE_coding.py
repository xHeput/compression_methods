def kodujRLE(dane):
    wynik = ""
    licznik = 0
    c = dane[0]
    for i in range(len(dane)):
        if (dane[i] == c):
            licznik += 1
        else:
            wynik = dopisz(wynik, c, licznik)
            c = dane[i]
            licznik = 1
    wynik = dopisz(wynik, c, licznik)
    return wynik


def dekodujRLE(dane):
  wynik = ""
  i = 0
  while(i < len(dane)):
    if (dane[i] == ';'):
      i += 1
      a = 0
      while (i < len(dane) and dane[i] != ';'):
        a = a * 10 + ord(dane[i]) - ord('0')
        i += 1
      while (a > 1):
        wynik += wynik[len(wynik) - 1]
        a -= 1
    else:
      wynik += dane[i]
    i += 1
  return wynik


def dopisz(data, c, licznik):
    if (licznik > 0):
        data += c
        if (licznik > 1):
            data += ";" + str(licznik) + ";"
    return data


dane = input("Podaj dane do kompresji:\n")
zakodowane = kodujRLE(dane)
print("Po kompresji:\n" + zakodowane)
dekodowane = dekodujRLE(zakodowane)
print("Po dekodowaniu:\n" + dekodowane)
