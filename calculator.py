#**** Making a simple calculator for general purpose*****
def add(a,b):
    add= a+b
    return add
def sub(a,b):
    sub=a-b
    return sub
def mul(a,b):
    mul=a*b
    return mul
def div(a,b):
    div=a*b
    return div

#Asking for add multipy subtract and div
q=int(input('1. add 2. sub 3.mul 4.div'))
print(q)
if q>4:
    print('wrong input')
    exit()

#Taking inputs from user
repeat='y'
while repeat=='y':
    a=int(input('first number '))
    b=int(input('second number '))
    if q==1:print('add is ',add(a,b))
    elif q==2:print('sub is ',sub(a,b))
    elif q==3:print('mul is ',mul(a,b))
    elif q==4:print('div is ',div(a,b))
    repeat=input('Do you want to another trip [y/n]')

