from superBetScrapper import extractSuperbetData
from uniBetScrapper import extractUniBetData

listaSuperBet = extractSuperbetData()
listaUniBet = extractUniBetData()

listOfSameMatches = []

for m in listaSuperBet:
    for n in listaUniBet:
        if(m.compare(n) == True):
            listOfSameMatches.append([m,n])

for mt in listOfSameMatches:
    print(mt[0], mt[1])