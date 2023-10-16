a = [3,4,5,6,3,8,10]
b = ['Zebra','apple','zebra','Apple']
a.sort()
b.sort()
print(a)
print(b)

a.sort(reverse=True)
print(a)
sorted_string = ','.join(b)

str_a = map(str,a)
print(','.join(str_a))

print(sorted_string)