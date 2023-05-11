# from email.policy import default
import matplotlib.pyplot as plt
import numpy
import random

# 1. plot with default coord of x and given y-axis coord
# plt.plot([1,2,3,4,5])
# plt.show()

# 2. with both x and y-axis input 
# plt.plot([1,2,3,4,5],[1,4,9,16,25])
# plt.show()

# 3. Changing the properties of plot line
# plt.plot([1,2,3,4,],[2,4,6,8],'bs-')
# plt.show()

# 4. title and plot names

# plt.title("P=k/V")
# plt.xlabel('Pressure',fontsize = 12,color='red')
# plt.ylabel('Volume',fontsize = 12,color='green')
# plt.plot([1,2,3,4,],[2,4,6,8],'bs-')
# plt.axis([0,6,0,8])
# plt.grid(True)
# plt.show()

# Example to plot with values
# x = [i for i in range(20)]
# x = numpy.array(x)
# plt.plot(x,x**2,'r-',x,x**3)
# plt.show()

# Scatter Plot
x = [random.randint(1,50) for i in range(20)]
y = [random.randint(1,50) for i in range(20)]
plt.axis([0,50,0,50])
# plt.scatter(x,y)
plt.bar(x,y)
plt.show()
