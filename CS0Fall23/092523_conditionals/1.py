def grade_calc(grade):
    if grade < 60:
        letter = 'F'
    elif grade < 70:
        letter = 'D'
    elif grade < 80:
        letter = 'C'
    elif grade < 90:
        letter = 'B'
    else:
        letter = 'A'
    
    return letter

def bad_grade_calc(grade):
    if grade <= 100:
        letter = 'A'
    elif grade <= 90:
        letter = 'B'
    elif grade <= 80:
        letter = 'C'
    elif grade <= 70:
        letter = 'D'
    else:
        letter = 'F'
    
    return letter

def main():
    a = 15
    b = 10

    if a<b: # one way selecter
        print("a is less than b")
        # let's say we want to end the program if a<b
        return
    
    if b==9:
        print(b)

    print("The rest of the program")

    grade = float(input("Please enter how manys points you got out of 100,\nand I'll tell you your letter grade.\n"))

    if grade > 0:
        if grade < 100:  # nested conditional 
            #calculate the grade
            letter = grade_calc(grade)
            
            print("You got a ", letter, '!')

            letter = bad_grade_calc(grade)
            print("You got a ", letter, '!')
    else:
        print("Invalid input.")




    
    
    


main()