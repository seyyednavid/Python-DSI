

###############################################
# Mathplotlib - Histograms
###############################################


import matplotlib.pyplot as plt
import pandas as pd


body_data = pd.read_csv("weights_and_heights.csv")

body_data.describe()


male = body_data[body_data["Gender"] == "Male"]
female = body_data[body_data["Gender"] == "Female"]


plt.style.use("seaborn-v0_8-poster")
plt.hist(male["Weight"], bins = 20, edgecolor = "black", alpha = 0.6, color = "royalblue", label = "male")
plt.hist(female["Weight"], bins = 20, edgecolor = "black", alpha = 0.6, color = "magenta", label = "female")
plt.title("Distribution of Body Weight by Gender")
plt.xlabel("Weight (lbs)")
plt.ylabel("Frequency")
plt.grid(False)
plt.legend()
plt.tight_layout()
plt.show()