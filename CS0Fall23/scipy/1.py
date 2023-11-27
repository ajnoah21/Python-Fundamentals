import numpy as np
import matplotlib.pyplot as plt

nums_x = [0,1,2,3,4]
nums_y = [0,1,4,9,16]

arr_nums_x = np.array(nums_x)
arr_nums_y = np.array(nums_y)

print(arr_nums_x)
print(arr_nums_y)

added = []
for i in range(len(arr_nums_x)):
    added.append(arr_nums_x[i]+arr_nums_y[i])

print(added)
print()

print(arr_nums_y+arr_nums_x)

plt.plot(arr_nums_x, arr_nums_y+arr_nums_x)

plt.show()