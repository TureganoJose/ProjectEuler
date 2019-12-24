# def modulo(inputnum, number):
#    div = int (inputnum/number)
#    return inputnum - (div * number)
import time


def getsum(n):
    total = 0
    while (n != 0):
        total = total + int(n % 10)
        n = int(n / 10)
        if total > 23:
            break
    return total


start = time.time()

sumDigits = 0
sumNumbers = 0
iNum = 23
while iNum < 1*(1e42):
    #    StringNumber = str(iNum)

    #    for iPosition in range(len(StringNumber)):
    #        sumDigits = sumDigits + int(StringNumber[iPosition])
    #        if sumDigits > 23:
    #            break
    #       print(iNum, sumDigits)
    #    if sumDigits == 23:
    #        sumNumbers += 1
    #       print(iNum)
#   if getsum(iNum) == 23:
#        sumNumbers += 1
    #    sumDigits = 0

    iNum += 23
print(sumNumbers)
print(sumNumbers % 1e9)

end = time.time()
print(end - start)
