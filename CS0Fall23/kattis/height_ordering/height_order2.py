'''
Name: Corin Chepko
Date: 10/18/23
Program Description: https://open.kattis.com/problems/height
Algorithm:
    input number of sets
    for each set:
        input 21 integers
        first integer is set_number
            make a set containing first number
            steps=0
            for all the rest of the numbers:
                for each number in ordered set, counting from the end,
                    insert number in front of first number bigger than it,
                    and add number of people behind to steps
                    if no greater number, add number to the end
                    
        '''
def test():
    pass

def main():
    number_of_sets = int(input())
    for z in range(number_of_sets):
        #collect line of 21 integers
        line = input().split()
        line = list(map(int, line))
        set_number = line[0]
        numbers = line[1:]
        #print(set_number,numbers)

        steps=0
        ordered = [numbers[0]]
        #print(ordered)
        for i in range(1,20):
            #for j in range(len(ordered)):
            index=0
            added = False
            for s in ordered:
                if(numbers[i] < s):
                    #steps = steps + j+1
                    steps = steps + len(ordered[index::])
                    ordered.insert(index,numbers[i]) #found someone shorter, insert height in front
                    added = True
                    break
                if(not added):
                    ordered.append(numbers[i])
                    break
                index = index+1
        print(f"{set_number} {steps}")
        #print(set_number,steps)


# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()