## Multiples of 3 and 5
## Problem 1

##If we list all the natural numbers below 10 that are multiples of 3 or 5,
##we get 3, 5, 6 and 9. The sum of these multiples is 23.
##
##Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
n = 1
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        total = total + n
    n = n + 1
print(total)

summ = []
i = 1
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        summ.append(i)
    i = i + 1
print(sum(summ))

