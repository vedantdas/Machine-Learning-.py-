sum =0
for x in range(1000):
    #print("x =", x)
    if (x % 3 == 0) or (x % 5 == 0):
        #print("x after condition =", x)
        sum=sum + x
        #print('sum =', sum)
print("Sum of Multiple of 3 and 5 =",sum)