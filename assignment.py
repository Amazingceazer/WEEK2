
#QUESTION1

my_age= 30
pi=3.14159

magic_number=(my_age *3 + 3.14159 % 7)

print (type(magic_number))
print (magic_number)


#QUESTION2

secret_word="PythonIsAmazing"

print ("PythonIsAmazing"[:-9])

print ("PythonIsAmazing"[-7:])

print ("PythonIsAmazing" [-9:-7]) 

print ("PythonIsAmazing"[-6:-8])

print ("PythonIsAamazing"[0:6:2])

#indexing

print (secret_word [len(secret_word)-1])

print (secret_word[-7])
print (secret_word[-6])
print (secret_word[-5])
print (secret_word[-4])
print (secret_word[-3])
print (secret_word[-2])
print (secret_word[-1])




print ("PythonIsAmazing"[::2])

print ("PythonIsAmazing"[::-1]) #reverse string

print ("PythonIsAmazing" [1:15:2]) #Everysecond character in a string


#QUSTION3

secret_word="PythonIsAmazing"
firstString = "Python"
secondString= "IsAmazing"

print(firstString.upper());

print(secondString.lower())

print(firstString.upper() +  secondString.lower())




first_name = "python"
first_name = first_name.capitalize()
print(first_name)

first_name = "python"
print (first_name.capitalize() + first_name.uppercase()[::])
