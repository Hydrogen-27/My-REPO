
import math,random
def generateASM() :
    Digits = "0101010101"
    ASM = ""
    for i in range(100000) :
        ASM += Digits[math.floor(random.random() * 10)]
    return ASM
while __name__ == "__main__" :     
    print("\033[32m", generateASM())
while __name__ == "__main__" :     
    print("\033[32m", generateASM())

    