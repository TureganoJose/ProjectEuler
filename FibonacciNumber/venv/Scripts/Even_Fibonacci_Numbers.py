def fibs(n):
    fibs = [0, 1, 1]
    for f in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

FiboNum = 0
n = 0
TotalSum = 0
while FiboNum  < 4e6:
    remainder = int( FiboNum % 2)
    if remainder == 0:
        TotalSum += FiboNum
    FiboNum = recur_fibo(n)
    n += 1
print(TotalSum)

