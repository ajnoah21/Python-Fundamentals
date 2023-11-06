# File IO examples

print("Hello World!")

with open("dict-words.txt", 'r') as fin:
    #line = fin.readline()
    #data = fin.read()
    lines = fin.readlines()
    
for line in lines:
    print(line.strip())
#print(data)
#print(type(data))
#print(line)

# newer and better syntax - preferred way!!
alist = [1, 2, 3]
with open('words.txt', 'w') as fout:
    fout.write('apple\nball\ncat\ndog\n')
    fout.write('elephant\n')
    fout.write('zebra\n')
    fout.write(str(1))
    fout.write('\n')
    fout.write(str(alist))