def readDataline():
    line = input().split()
    set_num = int(line[0])
    numbers = list(map(int,line[1:]))
    return set_num, numbers

def height_ordering(numbers):
    steps = 0
    ordered = [numbers[0]]
    for i in range(1,len(numbers)):
        for j in range(len(ordered)):
            if(numbers[i] < ordered[j]):
                steps = steps + len(ordered)
                ordered.insert(numbers[i])
            else:
                ordered.append(numbers[i])
        
    return steps

num_lines = int(input())

set_num,numbers = readDataline()
#print(set_num, numbers)
steps = height_ordering(numbers)
print(set_num,steps)