# Corin Chepko
# 2/22/23
# Kattis: Count the Vowels
# Algorithm steps: 1) input a string of input 2) loop through string
# check if character is a vowel 3) If character is a vowel,
# increment count variable 4) Print count

my_string = input()
count = 0
#for c in my_string:
#    print(c)
#    if( c.lower() == 'a' or c.lower() == 'e' or
#    c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u'):
#        count += 1

count += my_string.count('a')
count += my_string.count('e')
count += my_string.count('i')
count += my_string.count('o')
count += my_string.count('u')
count += my_string.count('A')
count += my_string.count('E')
count += my_string.count('I')
count += my_string.count('O')
count += my_string.count('U')

print(count)