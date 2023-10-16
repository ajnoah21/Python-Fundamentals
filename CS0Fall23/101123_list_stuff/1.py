import string

print(string.digits)
print(string.ascii_lowercase)
print(type(string.ascii_letters))
print(list(string.ascii_letters))

alpha = list(string.ascii_letters)

first_8 = alpha[0:8] # slices up but not including the 8th index
print(first_8)
print()
even_letters = alpha[::2]
print(even_letters)
print()
print(even_letters[-1]) # index of -1 is last thing on list

nums = [0,1,2,3]
print(nums[-4]) # can access list indices up to positive len(list)-1 and negative len(list)
print(nums[3])

name = ["Corin Chepko","someone else"]
l_name = "Chepko"

first_5_chars = name[0:5]
print(first_5_chars)
name[0] = "Rick"
print(name)