from matplotlib import pyplot as plt
from numpy.random import randint
x = [1,2,3,4,5]
data1_y = [1,6,22,66,111]

data2_y = randint(1,120,5)

plt.plot(x, data1_y)
plt.plot(x, data2_y)

plt.legend(["Fixed numbers", "Random numbers"])

plt.title("Some data!")
plt.xlabel("index")
plt.ylabel("Data")
plt.show()