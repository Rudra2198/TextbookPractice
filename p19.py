def Square1(x):
    
    result = x ** 2

    return result

def Square2(a=2):
    ans = a ** 2

    return ans

def summ(*num):
    sum1 = 0
    for i in num:
        sum1 += i

    return sum1

n = int(input("Enter input : "))

S1 = Square1(n)
S2 = Square2()

print("The square of ",n," is ",S1)

print(S1+S2)
print(summ(100,200,300,400,500))

