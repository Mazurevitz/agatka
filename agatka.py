agatka = "agatka"
if(agatka.count('a') == 3):
    agatka = agatka.replace('a', 'p')
    size = len(agatka)
    # Slice string to remove last character from string
    agatka = agatka[:size - size + 1]

to = "bloczydło"
to = to.replace('blocz', '')
to = to.replace('dło', '')

moja = "ramen"
moja = moja[0]

malenka = "przyczepka"
if (malenka.find('p') == 7):
    malenka = "kolinka"
else:
    malenka = "eczka"
    
rozwiazanie = ''.join([agatka, to, moja, malenka])

print(rozwiazanie)