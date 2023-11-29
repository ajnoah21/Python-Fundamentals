import pathlib
import matplotlib.pyplot as plt
import numpy as np

my_path = pathlib.Path(__file__).parent.resolve()
filename = f"{my_path}/weather.csv"

# If all of your columns are the same type:
#x = pd.read_csv(filename, header=0).values
#print(x)
x = []
y = []
with open(filename) as data:
    headers = data.readline().split(sep=',')
    lines = data.readlines()
    #print(lines)
    for i in range(len(lines)):
        line = lines[i].strip().split(sep=',')
        x.append(line[0].split()[0])
        y.append(line[2])

#print(x)
#print(y)
print(len(x))
x = np.array(x)#(list(map(float,x)))
y = np.array(list(map(float,y)))
x = x[::-1]
y = y[::-1]
plt.plot(x[0::287],y[0::287],color='blue')
plt.xticks(rotation=70, ha='right')
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.title("Plot of CSV data")
plt.show()