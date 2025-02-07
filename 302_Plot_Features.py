

###############################################
# Mathplotlib - Additional Plot Features
###############################################


import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_squared = [x ** 2  for x in x_values]
x_cubed = [x ** 3  for x in x_values]

plt.plot(x_values, x_squared, label = " X Squared" )
plt.plot(x_values,x_cubed , label = " X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The values of x")
#plt.xlim(2,8)
plt.xticks(range(11))
plt.ylabel("The values of y")
#plt.ylim(-100,600)
plt.legend()
plt.show()


# create a plot without number (xticks & yticks) - useful in certain cases where we want to show off a trend without giving any confidential numbers 
plt.plot(x_values, x_squared, label = " X Squared" )
plt.plot(x_values,x_cubed , label = " X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The values of x")
#plt.xlim(2,8)
plt.xticks([])
plt.ylabel("The values of y")
#plt.ylim(-100,600)
plt.yticks([])
plt.legend()
plt.show()


# Add grid - it does not work with  plt.xticks([]) & plt.yticks([])
plt.plot(x_values, x_squared, label = " X Squared" )
plt.plot(x_values,x_cubed , label = " X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The values of x")
plt.ylabel("The values of y")
plt.grid(True)
plt.legend()
plt.show()