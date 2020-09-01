### In this we will learn about dictionary work ###
"""Dictionaries are mutable in python3"""
dict1={'Surjit':'Urdan','sanju':'wazidpur','Rahul':'Bangladesh','Babbu':{'Born':"Urdan",'permanent':'Urdan',"Temporary":'Kharar'}}
print(dict1)
print(dict1['Babbu'])
print(dict1['Babbu']['Born'])

#Adding a new element in dictionary
dict1['Happy']='Hospital Rajpura'
print(dict1)

#Deletin number
del dict1['Happy']
print(dict1)


#Dictionary copies concept
#dict2=dict1
#del dict2['Babbu']
#dict2 is pointer to same memory location not a copy of dictionary 
#print(dict1)
#see it has deleted file from dict1 so keep in my

# How to tackle this problem
dict2=dict1.copy()
del dict2['Babbu']
print('This is dict2',dict2)
print('This is dict1',dict1)


#Another method to update the dictionary
dict2.update({'Leena':'America'})
print(dict2)


#how to print keys of dictionary
print(dict2.keys())