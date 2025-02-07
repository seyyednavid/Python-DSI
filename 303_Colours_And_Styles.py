

###############################################
# Mathplotlib - Plot Colours & Styles
###############################################


import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_squared = [x ** 2  for x in x_values]
x_cubed = [x ** 3  for x in x_values]


plt.style.available # List of styles for showing charts
plt.style.use('seaborn-v0_8-poster')

plt.plot(x_values, x_squared, label = " X Squared")
plt.plot(x_values, x_cubed , label = " X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The values of x")
plt.ylabel("The values of y")
plt.legend()
plt.show()


# plt.plot(x_values,x_cubed , label = " X Cubed", color = [1.0,0.5, 0.25]) RGB

# plt.plot(x_values, x_squared, label = " X Squared", color = "deeppink", linewidth = 2, linestyle = "--")
# plt.plot(x_values, x_cubed , label = " X Cubed", color = "#0000FF",  linewidth = 2, linestyle = ":")


# plt.plot(x_values, x_squared, label = " X Squared", color = "deeppink", linewidth = 2, marker = "." )
# plt.plot(x_values, x_cubed , label = " X Cubed", color = "#0000FF",  linewidth = 2, marker = "o",
#                                             markersize = 10, markerfacecolor = "red", markeredgecolor = "green")