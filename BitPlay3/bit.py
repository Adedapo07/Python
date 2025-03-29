def divide(dividend,Divisor):
    sign=(-1 if((dividend<0)^(Divisor<0))else 1)
    dividend = abs(dividend)
    Divisor = abs(Divisor)

    quotientNumber = 0
    tempNumber = 0
    for i in range(31,-1,-1):
        if(tempNumber +(Divisor << i )<= dividend):
            tempNumber += Divisor << i
            quotientNumber |= 1 << i
        if sign == -1:
            quotientNumber = -quotientNumber
        return quotientNumber
    
a = int(input("Enter a for a/b:"))
b = int(input("Enter b for a/b:"))
print("Result of",a,"1",b, "is" , divide (a,b))