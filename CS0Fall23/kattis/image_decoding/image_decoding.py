'''
Name: Corin Chepko
Date: 10/23/23
Program Description: https://open.kattis.com/problems/imagedecoding
'''
def test():
    pass

def main():
    pix_sym = ('#','.')
    scan_lines = int(input())
    while(scan_lines != 0):
       pixels = 0
       image = []
       error_cond = False
       last_num_pix = 0
       for i in range(scan_lines):
            num_pix_in_line = 0
            
            line = input().split() 
            out_line = ""
            if(line[0] == '#'):
                sym = 0
            else:
                sym = 1
            
            for index in range(1,len(line)):
                added = pix_sym[sym]
                added = added*int(line[index])
                num_pix_in_line += int(line[index])
                out_line += added
                sym = (sym+1)%2
            print(out_line)
            if((i!=0) and (num_pix_in_line != last_num_pix)):
                error_cond = True
            last_num_pix = num_pix_in_line
       if(error_cond == True):
           print("Error decoding image")
       else:
           print() 
       scan_lines = int(input())

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()