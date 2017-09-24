import matplotlib.pyplot as plt
import numpy as np
year = [1950, 1970, 1990, 2010]
pop =[ 2.519, 3.692, 5.263 , 6.972]
a, b = np.polyfit(year, pop, 1)
new=[]
year1=[]
for i in range (0,30):
    year1.append(1950 + 10 * i)
    new.append(year1[i]*a + b)
plt.plot(year1, new)
plt.show()
print("hello world")