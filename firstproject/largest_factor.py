def largest_factor(n):
    factors = []
    for i in range(n):
        if i ==0:
            continue
        if n%i == 0:
            factors.append(i)
    factors.sort()
    largest_factor = factors[-1]
    
    if len(factors) == 1:
        print("Factor is: ", end="")
    else:
         print("Factors are: ", end="")
    for i in factors:
        if i == largest_factor:
            print(i)
            print("The largest factor is "+str(largest_factor))
            break
        print(i, end=",")
        

largest_factor(80)
print(eval(str(8)+str(6)))
print(eval("3"+"7"))
    
        