def fibonacci():
    count = 0
    numb1, numb2 = 0, 1
    vraag = int(input("Hoeveel keer?"))
    if vraag >= 1:
        print("Fibonacci =")
        while count < vraag:
            antwoord = numb1 + numb2
            numb1 = numb2
            numb2 = antwoord
            count += 1
            print(numb1)
    else:
        print("Het getal moet hoger zijn!")
    
fibonacci()
input("Druk op enter om te stoppen")

        
