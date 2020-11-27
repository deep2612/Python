#While Loop
n = 5
while(n > 0):
    print("Inside while loop : ", n)
    n -= 1

#Break Statement
m = 5
print("Break Statement Example")
while(m > 0):
    if(m == 2):
        break
    else:
        print(m)
    m -= 1

#Continue Statement
p = 5
print("Continue Statement Example")
while(p > 0):
    p -= 1
    if(p == 4):
        continue
    print(p)
