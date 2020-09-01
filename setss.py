# a set stores unique values 
s=set([1,3,2,3,2,1])
print(s)
#it will not show one value again and again 
s.add(971)#this will be added
s.add(1)# this is not because its same
print(s)
s.remove(1)#to remove the element
print(s)

#mainly it is used for set like union intersection etc.
