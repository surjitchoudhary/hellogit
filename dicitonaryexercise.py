words={'PM':'Narendra Modi','President':'Ram Nath Kovind','FM':'SithaRaman','HM':'Amit Shah','CM':'Captain Amrinder Singh'}
print(words)
a='y'
while(a=='y' or 'Y'):
    key=input('Enter the key words PM,President,FM,CM,HM            ')
    print(words[key])
    a=input('Do you want to know more words [y/n]')