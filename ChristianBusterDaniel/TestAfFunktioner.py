import math
gemtetal= [154,103]
nyttal=(float(input(" > ")))

gemtetal.append(nyttal)
def Testafmangetal(liste):
    result = 0
    længde= len(liste)
    result= sum(liste)
    result= result/længde
    return (result,længde)

print(Testafmangetal(gemtetal))

