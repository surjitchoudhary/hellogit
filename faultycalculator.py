def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
def rem(a,b):
    return a/b


op=int(input('Press 1 = add, 2 = subtract, 3 = multiply, 4 = divide, 5 remender'))
if (op<1 and op>5):
    print('Input is wrong ')
    exit()

value1=int(input('Enter the value of first element'))
value2=int(input('Enter the value of second element'))

if value1==45 and value2==3 and op==3:
    print('555')
    exit()


elif value1==56 and value2==9 and op==1:
    print('77')
    exit()

elif value1==56 and value2==6 and op==4:
    print('4')
    exit()


if op==1:
    print(add(value1,value2))
elif op==2:
    print(sub(value1,value2))
elif op==3:
    print(mul(value1,value2))
elif op==4:
    print(div(value1,value2))
elif op==5:
    print(rem(value1,value2))