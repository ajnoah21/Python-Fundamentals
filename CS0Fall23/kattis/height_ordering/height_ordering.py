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

    for k in range(number_of_sets):
        line = list(map(int,input().split()))
        set_num = line[0]
        nums = line[1:]

        #print(set_num, nums)
        ordered = [nums[0]]
        #print(ordered)
        steps = 0

        for j in range(1,20):
            i = len(ordered)-1
            while(i>=0):
                if nums[j] < ordered[i]:
                    steps = steps + len(ordered)
                    ordered.insert(i,nums[j])
                    break
                if i == 0:
                    ordered.append(nums[j])
                i = i-1
        print(set_num,steps)
        

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()