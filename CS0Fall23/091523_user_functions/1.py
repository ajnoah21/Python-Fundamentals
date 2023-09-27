'''
Definining functions examples
'''

# Fruitless function, doesn't return any data
def hello():
    print("Hello World!")

# Fruitless function, does take data, still doesn't return data
# no default data included
def custom_hello(message):
    print(message)

# Fruitless function, does take data, still doesn't return data
# default data provided
def custom_hello2(message='Anonymous'):
    print(message)

def sum_two(a, b):
    answer =  a+b
    return answer

def sum_three(a, b, c):
    global e
    e=2
    answer =  a+b+c+e
    return answer


hello()
custom_hello("Hello")
c, d, e = input("Enter three numbers separated by a space: ").split()
c = float(c)
d = float(d)
e = float(e)
ans = sum_two(c, d)
print(ans)
print(sum_two(c,d))

print(sum_three(c, d, e))
print(e)