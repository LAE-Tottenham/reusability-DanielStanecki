
import math

def sideinput(nth, sidetype):
    side = float(input("Enter your " + nth + " triangle's "+ sidetype + " side length: "))
    return side

def pythagorus(opp, adj):
    hyp = math.sqrt(opp**2 + adj**2)
    return hyp

