phrase2 = ''' \'\'\' '''  
# triple single quotes or double quote can using almost anything expect more triple qoutes

phrase = "'What\'s up\n Shaq O\'Neal?"

print(phrase2)
print(phrase)

phrase3 = "My solution is\t\rbonkered.\n"
print(phrase3)

time = 111
hours = 111//60
minutes = 111%60
print("111 minutes = ")
print(hours,minutes)

random_number = 100
random_number % 10 # the result of this will always be between 0 and the second number

print("2 to 3rd power =  ", 2**3)
print("2 XOR 3 =  ", 2^3) # the ^ is an XOR operation

# Some examples
fname = "John"
lname = "Smith"
fullName = fname + ' ' + lname + " " #can add literal strings with variables that are strings
print(fullName)
print(fullName*5)

name = input("\nPlease enter your name: ")
print("Hello, " + name + "Nice to meet you!")
name_times = int(input("Enter how many times to print your name: "))
#name_times = int(name_times)
print(name_times*name)

next_line = name + "repeated " + str(name_times)
print(next_line)