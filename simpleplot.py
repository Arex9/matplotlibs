from xml.etree.ElementTree import Comment
from matplotlib import pyplot as plt
from numpy.random import randint

# Setting style of the plot
# See all styles by printing plt.style.available 
plt.style.use('ggplot')

x = [1,2,3,4,5]
data1_y = [1,6,22,66,111]

# Array of 5 elements randomized integers between 1 and 120
data2_y = randint(1,120,5)

plt.plot(x, data1_y,'k--', linewidth=1,label="Fixed numbers")
plt.plot(x, data2_y, 'b-o', linewidth=1, label="Random numbers")

# Apply legend labels
plt.legend()

# Title and layout
plt.title("Some data!") 
plt.xlabel("index")
plt.ylabel("Data")

# Grid 
plt.grid(True)

# Tight padding
plt.tight_layout()      

plt.show()