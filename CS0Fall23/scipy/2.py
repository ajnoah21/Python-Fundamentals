import numpy as np
import matplotlib.pyplot as plt
import math

x_vals = np.linspace(0, 2*math.pi, 100)
print(x_vals)

y_vals = np.sin(x_vals)

print(y_vals)

plt.plot(x_vals[0:50],y_vals[0:50], color="green")
plt.plot(x_vals[0:50],y_vals[0:50]+x_vals[0:50], color="red")
plt.title("My first Python Plot!")
plt.show()