def start(getal: int):
	getal = int(input("Van welk getal wilt je de tafel zien?"))
	for i in range(1,11):
		eind = getal*i
		print(str(getal) +" x "+str(i)+" = "+str(eind))

start('getal')
input("press enter to exit")