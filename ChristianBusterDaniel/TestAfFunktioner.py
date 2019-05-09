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

import pickle    # Kan gemme list på en fil


favorite_color = ["blue","yellow","green","red"]

pickle.dump(favorite_color, open("MinFile.p", "wb"))

favorite_color = pickle.load( open( "MinFile.p", "rb" ) )
