# Asumsi total self number merujuk ke banyak jumlah self number

def sumDigits(bil):
    result = 0
    while(bil != 0):
        result = result + bil%10
        bil = bil//10 
    return result

def checkSelfNumber(bil):
    for i in range(1, bil+1):
        if(i + sumDigits(i) == bil):
            return False
    return True

def totalSelfNumberBelow200():
    selfNumbers = []
    for i in range(1, 200):
        if(checkSelfNumber(i)):
            selfNumbers.append(i)
    return len(selfNumbers)

#print(totalSelfNumberBelow200())