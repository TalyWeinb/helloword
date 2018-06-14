import random
import math


#declare classe
class PIMonteCarlo:
    #déclare méthode
    def computePI(self, iteration):
        total = 0

        for i in range(1,iteration):
            x = random.random()
            y = random.random()
            dist = math.sqrt(x*x+y*y)

        if dist<=1:
            total = total+1

        pi = total / iteration *4

        return pi

#instancier la classe
myClass = PIMonteCarlo()

pi10 = myClass.computePI(10)
pi1000 = myClass.computePI(1000)

print(pi10)
print(pi1000)
