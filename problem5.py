def number_transformation(n, p, d):
    digit=str(n)[len(str(n))-p]
    digit=int(digit)
    if digit>=0 and digit<=4:
        digit+=d
        digit=int(str(digit)[-1])
    if digit>=5 and digit<=9:
        digit=abs(digit-d)
        digit=int(str(digit)[0])
    n=list(str(n))
    n[len(n)-p]=str(digit)
    for i in range((len(n)-p)+1, len(n)):
        n[i]='0'
    return int("".join(n))
print(number_transformation(7145032, 2, 8))
print(number_transformation(1540670, 3, 54))
