










#Strings are bits of text. They can be defined as anythi
astring = "Hello world!"
astring2 = 'Hello world!'

astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))#12



#count char in given string 
astring = "Hello world!"
print(astring.count("l"))#3

#indexing in srting  but can't change the string data 
astring = "Hello world!"
print(astring[3:7])

'''
for example want to change the index char by other 
copy and run from outside the comment 
astring[0]='r'
print(astring)
this show the error while once you run '''



'''

There is no function like strrev in C to reverse a string. But with the above mentioned type of slice syntax you can easily reverse a string like this

try please  
astring = "Hello world!"
print(astring[::-1])
this is same while code for palindrom the string 

'''


'''
try Copy and past outside the comment and run
astring = "Hello world!"

afewwords = astring.split("  ")

in split it will take some input as for which using you can split the string for
example comma(,)    undescore(_) etc 
'''












'''
lower case and upper case

try Copy and past outside the comment and run
astring = "Hello world!"
print(astring.upper())
print(astring.lower())'''







#follow this link for more with string 
'''https://www.w3schools.com/python/python_ref_string.asp'''
#Upper case the first letter in this sentence:

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


# See what happens if the first character is a number:
txt = "36 is my age."

x = txt.capitalize()

print (x)


#Make the string lower case:
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)





'''

next is based on  Conditions  like if else or using greater than equal to   
'''