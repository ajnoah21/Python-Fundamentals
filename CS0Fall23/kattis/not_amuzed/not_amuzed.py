'''
Name: Corin Chepko
Date: 11/01/23
Program Description: https://open.kattis.com/problems/notamused
Algorithm:
    Read input until EOF:
    if line == 'OPEN'
        until line == 'CLOSE':
            read line
            if line[0] == 'ENTER':
                add map entry for key as name, line[1], and value as line[2]
            if line[0] == 'EXIT'
                modify map[key] value with line[2]-value (minutes at park)

        After 'CLOSE':
            print day number
            print lines of names and what they owe 
'''

import sys

def test():
    pass

def make_report(day, customers):
    s_customers = dict(sorted(customers.items()))
    report = f"Day {day}"
    #print(f"Day {day}")
    for key,value in s_customers.items():
        report += f"\n{key} ${value*0.10:.2f}"
        #print(f"{key} ${value*0.10:.2f}")
    report += '\n'


    return report

def main():
    day = 0
    for line in sys.stdin:
        line = line[:len(line)-1]
        if line == "":
            break        
        if line == 'OPEN':
            day += 1
            line = input()
            customers = {}
            while line != 'CLOSE':
                line = line.split()
                if line[0] == 'ENTER':
                    if line[1] not in customers:
                        customers[line[1]] = int(line[2])
                    else:
                        customers[line[1]] = int(line[2]) - customers[line[1]]
                if line[0] == 'EXIT':
                    customers[line[1]] = int(line[2]) - customers[line[1]]
                line = input()
                if line == 'CLOSE':
                    report = make_report(day, customers)
                    print(report)
                    break

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()