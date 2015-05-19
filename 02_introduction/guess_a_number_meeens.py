from random import randint

counter = 0
versuche = 8
zahl = randint(1,99)
print 'Errate die Zufallszahl zwischen 0 und 100!'
print 'Du hast ' + str(versuche) + ' Versuche. Los gehts!'

while counter < versuche:
    guess = raw_input()
    guess = int(guess)

    counter = counter + 1

    if guess < zahl:
        
        print 'Zu klein! Du hast noch ' + str(versuche-counter) + ' Versuche!'

    if guess > zahl:

        print 'Zu gross! Du hast noch ' + str(versuche-counter) + ' Versuche!'

    if guess == zahl:
        break

#frage = 'Willst Du nochmal Spielen? Druecke J fuer Ja oder N fuer Nein:'
if guess == zahl:
    print('Super! Die Zahl lautet ' + str(zahl) + '.' + ' Du hast ' + str(counter) + ' Versuche gebraucht!')
    #counter = 0
    #print(frage)
if guess != zahl:
    print('Nope. Die Zahl lautet ' + str(zahl) + '.' + ' Du hast ' + str(counter) + ' Versuche gebraucht!')
    #counter = 0
    #print(frage)
