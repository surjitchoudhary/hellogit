#indexing is important part in string in this course we will learn about index slicing 
str1 = "MY name is surjit"
print(str1)

""""IN python index starts from 0 
    so if you want to print particular character from a string you should have carefull about that."""
print(str1[0])
# In above it was the first character in string.
print(str1[-1])
# IN above it will print the last character in string.
print(str1[1:5])
# You can print a particular order of a string.from index 1 to 5


#how to know the length of string len
print(len(str1))

#one thing to note last string index will not matter all the times like in below example.
print(str1[0:1000])


"""Note: in case you find like str1[0:100:2] first two are from 0 to 100 and last say skip by 2 like in below given example"""
print(str1[0:17:2])


"""If you forget to take the first argument it will take 0 by default and in case you forget to put last in will take full size/"""
print(str1[:5])
print(str1[0:])

"""You cant take values in invert order like this"""
print(str1[-15:-7])

#Function
print(str1.isalnum())
#Above will return check the alpha value if it find it no space in it than it will return 'True' and 'False' 
#if you emit space from str1 strin and make it like 'MYnameissurjit' Than it will show True.
print(str1.isalpha())


#check with endswith() if your string ends with the given string it will print True and False if not
print(str1.endswith("surjit"))

#if you want to count the character in string use 'count()'
print(str1.count('s'))

#if you want to capitalize the first character of your string
str2="my name is surjit"
print(str2.capitalize())


#if you want to find something from string you can use'find'
print(str1.find('i'))

#if you want to make your string in lower case letter.
print(str1.lower())

# if you want to make your Strin in Upper case Letter.
print(str1.upper())

# If You Want To Make Your String Replace A Letter With Another Letter.
print(str1.replace('is','are'))