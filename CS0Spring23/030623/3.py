odd_0_20 = [x for x in range(0,21) if x%2 == 1]
print(odd_0_20)

sentence = 'the quick brown fox jumps over the lazy dog'

wlist = [ (w.upper(), w.lower(), len(w)) for w in sentence.split()]

print(wlist)

num_list = input("Enter numbers separated by a space").split()

print(num_list)
index = 0
for item in num_list:
    num_list[index] = int(item)
    index+=1

print(num_list)

num_list2 = list(map(int, input("Enter more numbers separated by a apce").split())) #for each item in the input, it converts it to an int, and returns a list

print(num_list2)
