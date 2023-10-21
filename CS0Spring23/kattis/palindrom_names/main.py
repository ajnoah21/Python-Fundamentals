# Corin Chepko
# 2/24/23
# 1) input name
# 2) check if it is a palindrome
# 3) for the input, without adding a character, we want to count how many changes need to be made to the second half
#   if it's an odd numbered input, we compare the same reversed half, with the end of the input string
# 4) Do the same for the input_string plus its first character, and compare changes.

def is_pali(line):
    r_line = line[::-1]
    if(line == r_line):
        return True
    else:
        return False

def test_pali():
    assert(is_pali("anna") == True)
    assert(is_pali("corin") == False)
    assert(is_pali("kaikiak") == True)
    #print("All tests passed.")

def count_changes(input):
    halfway = int(len(input)/2)
    sub_str = input[0:halfway]
    r_sub_str = sub_str[::-1]
    r_input = input[::-1]
    #print(input_line, r_sub_str)
    index = 0
    changes = 0
    #print(r_input)
    #print(sub_str)
    for c in r_input:
        if( c != sub_str[index]):
            changes = changes + 1
        index += 1
        if(index == len(sub_str)):
            break
    return changes

def test_count_changes():
    assert(count_changes("dedgfedcba") == 5)
    assert(count_changes("abcdefgdeda") == 3)
    assert(count_changes("corndawg") == 4)
    assert(count_changes("ana") == 0)
    assert(count_changes("kaikia") == 3)
    assert(count_changes("freddief") == 2)
    #print("All test_count_changes tests worked!")


test_pali()
#test_count_changes()

input_line = input()

ans = 100

if(is_pali(input_line) == True):
    ans = 0
elif(is_pali(input_line + input_line[0]) == True):
    ans = 1
elif(is_pali(input_line + input_line[1] + input_line[0])):
    ans = 2
elif(is_pali(input_line + input_line[2] + input_line[1] + input_line[0])):
    ans = 3
else:
    changes0 = count_changes(input_line)
    r_input_line = input_line[::-1]
    changes1 = count_changes(r_input_line)
    input_line = input_line + input_line[0]
    changes2 = count_changes(input_line) + 1
    r_input_line = input_line[::-1]
    changes3 = count_changes(r_input_line) + 1

    #print(f"Input: {changes0}, RInput: {changes1}, Inputplus1: {changes2}, RInputplus1: {changes3}")
    
    min = ans
    if( changes0 < min):
        min = changes0
    if( changes1 < min):
        min = changes1
    if( changes2 < min):
        min = changes2
    if( changes3 < min):
        min = changes3
    
    ans = min

print(ans)
