from random import *

def spongebobCase(str):
    bob = ""
    i = 0
    case = randint(0, 1)
    while(i < len(str)):
        if(case == False):
            bob += str[i].lower()
            case = True
        elif(case == True):
            bob += str[i].upper()
            case = False
        i += 1
    return bob

print("Ecrit un truc :")
input = input()
result = spongebobCase(input)
print (result)