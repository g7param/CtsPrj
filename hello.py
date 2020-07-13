import sys
import random
def convString(CS):
    if len(CS) > 8:
        print("Invalid string: greater thatnn 8 chars")
    else:
        try:
            print(int(CS))
        except:
            print("Enter bit string")
def pick8Cells():   
    lines = ['a','b','c','d','e','f','g','h']
    cell= []
    for i in range(8):
        cell.append(lines[random.randrange(8)] + lines[random.randrange(8)])
    return cell


print(pick8Cells())

