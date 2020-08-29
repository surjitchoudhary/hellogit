"""

List are mutable

Here we learn about making list"""
list1=['surjit','mandeep','kuldeep','ramandeep','hello']
print(list1)
#call by index
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
#Below will give an error which is IndexError:list index out of range
#print(list1[5])

#Now we try to print with negative number
print('this is using minus(-)',end=" ")
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
print(list1[-5])





### another  list in python mixed with numbers lets see what will happen
list2=['my','name','surjit','singh','Roll No.',19,123.4]
print(list2)
print(list2[-2]*10)
#so our above example succeed we can put numbers in list
print(list2[-1]+34.4)
# yes we can also add float value 
print(list2[1]+list2[3])
# we can also add strings in list



########################FUNCTION#############################
#print(list2.sort())
#Above will produce an error can't sort numbers and strings

numbers=[94,53,23,23,22,1,2,4,5]
numbers.sort()
print(numbers)
# IT will make permanent changes to list
numbers.reverse()
print(numbers)
#It will reverese the order in the string



#####slicing######
numbers=[1,3,4,3,5,7,456,77,34,223,2,2]
print(numbers[0:10])
print(numbers[:32])
print(numbers[2:4])
# above will print 2 and 3rd element 


print(numbers[::-2])
#first it will reverse the output than skip by 2


print(numbers[0:12:-1])
#now it will display empty list

print(len(numbers))
# len() usage

numbers.append('append')
print(numbers)
#it will add at the end 

"""
#making an empty list and ask user to add the numbers
i=0
emptylist=[]
n=int(input("How many attributes you want to add in your list"))
while i<n:
    emptylist.append(int(input('enter the number')))
    i=i+1
print(emptylist)

"""
#you can add more number in the list by using 'insert' function
list3=[1,2,3,4,5,6,7,8,9]
list3.insert(1,1)
print(list3)
#for above example
#insert(index,element)



###Remove###
list3.remove(1)
print(list3)
#it will remove first element with the same name
#it will give error if you submit something 


###Pop### 
list4=[1,3,4,2,34,32,1,21]
print(list4.pop())
print(list4)
#if pop() is empty it will pop the last element
#you can change the value of list till now

list4[3]=234234
print(list4)