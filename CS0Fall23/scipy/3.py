import numpy as np
import matplotlib.pyplot as plt
import math

x_vals = np.linspace(0, 10, 10)
print(x_vals)

with open("in_data.txt") as f_data:
    lines = f_data.readlines()
    y_vals = list(map(float, lines))
    np.array(y_vals)

plt.plot(x_vals,y_vals)
plt.show()