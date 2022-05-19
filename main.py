import random

listaA = []
listaB = []

listaC = []
listaD = []

for i in range (38):
    listaA.append(i + 74)
    listaB.append(i + 74)

for i in range (38):
    eleA = random.choice(listaA)
    listaA.remove(eleA)
    listaC.append(eleA)

    eleB = random.choice(listaB)
    listaB.remove(eleB)
    listaD.append(eleB)

for i in range (38):
    print(str(listaC[i]) + " com " + str(listaD[i]))

