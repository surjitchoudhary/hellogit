var1='hello'
var2=10
var3=12.4
#check the type of variables in python3 'str'=string,int=integer, float=decimal value
print(type(var1))
print(type(var2))
print(type(var3))

#we are here to check what kind of type does input BYDEFAULT TAKE
a=input('Bydefault str')
b=int(input('Enter integer value'))
c=float(input('Enter float value'))
d=str(input('Enter string '))
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#multiplying a string to an interger will print number of integer times the string.
"""Point to note here is float can't we multiplied by string it will give error if you want to try."""
print(a*b)
#Now we try string multiply by string
print(a*d)
#above equation will produce error Typeerror:can't multiply sequence by non-int of type 'str'.
