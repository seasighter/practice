# digits = [9]
digits=[9,9,9,9]
one = 1
i = 0
digits = digits[::-1]
while one:
    if i < len(digits):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i]+=1
            one = 0
    else :
        digits.append(1)
        one=0
    i+=1
    
print(digits[::-1])