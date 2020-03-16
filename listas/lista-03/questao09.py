a = int(input())
b = int(input()) 
c = int(input()) 

if a > b and a > c:
    d = a
    if b > c:
        e = b 
        f = c
    else:
        e = c 
        f = b 
elif b > a and b > c:
    d = b 
    if a > c:
        e = a 
        f = c 
    else:
        e = c 
        f = a 
elif c > a and c > b:
    d = c 
    if a > b:
        e = a 
        f = b 
    else:
        e = b 
        f = a 
