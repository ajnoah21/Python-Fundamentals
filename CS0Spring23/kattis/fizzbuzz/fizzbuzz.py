# Corin Chepko 
# Date: 2/17/23
# Kattis: Fizzbuzz
# Print numbers 1 to N, except if the number is divisable by X print "Fizz", 
# if it's diviable by Y, print "Buzz", if it's diviable by both print "FizzBuzz"

X, Y, N = input().split()
X = int(X)
Y = int(Y)
N = int(N)

for i in range(N):
    string = ""
    num = i+1
    if( num%X == 0 ):
        string += "Fizz"
    if( num%Y == 0 ):
        string += "Buzz"
    if( num%X != 0 and num%Y != 0):
        string = string + str(num)
    print(string)