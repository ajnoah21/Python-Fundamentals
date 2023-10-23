'''
Name: Corin Chepko
Date: 10/23/23
Program Description: https://open.kattis.com/problems/imagedecoding
'''
def test():
    pass

def main():
    scan_lines = int(input())
    while(scan_lines != 0):
       pixels = 0
       image = []
       for i in range(scan_lines):
           line = input().split() 
           out_line = ""
           for index in range(1,len(line)):
               out_line += int(line[i])*line[0]
       
       scan_lines = int(input())

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()