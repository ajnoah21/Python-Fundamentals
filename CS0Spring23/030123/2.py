l_inputs = ()

words = input("Enter a string with mutiple words").split()

for word in words:
    l_inputs = l_inputs + (word,)

print(l_inputs)
