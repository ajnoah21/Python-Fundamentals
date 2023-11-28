#input first line for number of watch button presses, N
#if number, N, is not odd, input N numbers
#if N is odd, print "still running"

#for every two numbers, find the difference.
#Add the differences.
#Print total difference

N = int(input())
if(N%2 == 1):
    print("still running")
else:
    i = 0
    diff = 0
    while True:
        t1 = int(input())
        t2 = int(input())
        diff += t2-t1
        i += 2
        if(i == N):
            break
    print(diff)
