
# Pandas - Exploring & Understanding our data

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")

transactions.shape # (38506, 6)
transactions.ndim  #  2

transactions.head() # returen first 5 rows
transactions.head(20)
transactions.tail() # returen last 5 rows

transactions.sample() # return one randomly selected row
transactions.sample(10)

# Important for getting sample data
sample = transactions.sample(frac = 0.1)  # (3851,6)


transactions.describe()  # quick overview


transactions.nlargest(5, "sales_cost")
transactions.nlargest(25, "sales_cost")

transactions.nsmallest(25, "sales_cost")

transactions.nunique()




customer_details = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")
customer_details.shape # (870, 4)

customer_details.head()

customer_details.describe()

customer_details.isna()
customer_details.isna().sum()









































