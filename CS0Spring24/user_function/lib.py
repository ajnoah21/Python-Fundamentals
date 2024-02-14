import random

names = ["Corin", "Scott", "Elizibeth", "Lydia", "Hi"]

def scott():
    rand_name = random.choice(names)
    return rand_name

def tony(num1, num2):
    sum = num1 + num2
    num1 = 20 #whatever happens to this local num1, stays local and doesn't affect the rest of the program
    return sum

card = "studlsnsflknSG"