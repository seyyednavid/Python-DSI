

# Pandas - Adding & Dropping Columns

import pandas as pd
transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")



# Adding columns

transactions["Store_id"] = 1

transactions["Profit"] = transactions["sales_cost"] * 0.2

import numpy as np
transactions["sales_type"] = np.where(transactions["sales_cost"] > 20, "Large", "Small")




condition_rules = [transactions["sales_cost"] > 50, transactions["sales_cost"] > 20, transactions["sales_cost"] > 10]
outcomes = ["X-Large", "Large", "Medium"]

transactions["sales_type"] = np.select(condition_rules, outcomes, default="Small") 



# Remove Columns

new_df = transactions.drop(["Store_id"], axis = 1)