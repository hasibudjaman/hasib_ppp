# print("hasib")
# print("github account")
# check if all number are prime
from itertools import count

num=[3,5,7,13]
count=0
for n in num:
    if n==0 or n==1:
        print("it is not prime number and False ")
        break
    elif n==2:
        len.append(n)

    if n>2:
        for i in range(2,n):

            if n%i!=0:

                count=0
                break

            else:
                count=1

if count==0:
    print(True)
elif count==1:
    print(False)
