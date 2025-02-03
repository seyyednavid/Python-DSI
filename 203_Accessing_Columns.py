

# Pandas - Accessing Columns

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")


"""
select 
    customer_id,
    sales_cost
from
    transactions

"""

# First way - Do not recommend
new_df = transactions.customer_id

my_var = "customer_id"
transactions.my_var # AttributeError: 'DataFrame' object has no attribute 'my_var'


# Second way

new_df = transactions["customer_id"]  # Series so it's not good as DataFrame is 2 dimentional
transactions[my_var]

new_df = transactions[["customer_id"]] # DataFrame


new_df = transactions[["customer_id", "sales_cost"]] # DataFrame








































