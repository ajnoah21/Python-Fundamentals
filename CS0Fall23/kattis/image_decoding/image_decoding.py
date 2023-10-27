'''
Name: Corin Chepko
Date: 10/23/23
Program Description: https://open.kattis.com/problems/imagedecoding
'''
def test():
    pass

def image_decode(scan_lines):
    pix_sym = ('#','.')
    pixels = 0
    image = []
    error_cond = False
    last_num_pix = 0
    for i in range(len(scan_lines)):
        num_pix_in_line = 0
        
        line = scan_lines[i] 
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
        #print(out_line)
        image.append(out_line)
        if((i!=0) and (num_pix_in_line != last_num_pix)):
            error_cond = True
        last_num_pix = num_pix_in_line
    if(error_cond == True):
        #print("Error decoding image")
        image.append("Error decoding image")
    else:
        image.append('\n')

    return image

def main():
    
    num_lines = int(input())
    if(num_lines != 0):
        scan_lines = []
        for i in range(num_lines):
            scan_lines.append(input())

        out_lines = image_decode(scan_lines)
        print(out_lines)
    else:
        return

    #while(scan_lines != 0):
        
   #    scan_lines = int(input())

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()