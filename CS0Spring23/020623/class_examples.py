num = int( input('Enter a number =>') )
print('You entered: ', num)
print('type of', num, '=', type(num))

num = int(num)
print("num = ", num)
print("num in binary = ", bin(num))
print("num in binary = ", hex(num))
print("num in binary = ", oct(num))

bin_number = 0b1010
not_bin_number = ~bin_number
print(not_bin_number)
print(bin(not_bin_number))


