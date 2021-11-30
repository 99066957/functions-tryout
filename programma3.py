def vraag(naam):
    naam = input("Wat is uw naam? Of typ STOP om te stoppen. : ")
    if naam == 'STOP':
        return naam
    leeftijd = input("Wat is uw leeftijd? Of typ STOP om te stoppen. : ")
    if leeftijd == 'STOP':
        return leeftijd
    print("Hallo " +str(naam) + " , je leeftijd is " +str(leeftijd)+ ".")

while True:
    vraag("naam")
    if vraag("naam") == 'STOP':
        input('Druk op enter om te stoppen.')
        break