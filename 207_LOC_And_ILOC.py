

#######################################
# Pandas - LOC & ILOC
#######################################

import pandas as pd
transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")

### transaction.loc[row_lables,column_lables]
### transaction.iloc[row_index,column_index]



### ILOC

transactions.iloc[0]
transactions.iloc[0:4]
transactions.iloc[[0,30,51]]
transactions.iloc[[0,30,51], 0:2]

transactions.iloc[0:4,[0,3,-1]]
transactions.iloc[:,[0,3,-1]]


### LOC

transactions.loc[0] # it works because index is zero and the lable for this index is also zero
transactions.set_index("customer_id", inplace=True)
transactions.loc[642] # return all rows that has customer_id = 642

transactions.reset_index(inplace=True)

list(transactions)

transactions.loc[0:10, "customer_id"]
transactions.loc[0:10, ["customer_id", "product_area_id", "sales_cost"]]
transactions.loc[0:10, ["product_area_id", "sales_cost", "customer_id"]] # in oeder to column order


### CONDITIONAL LOGIC

transactions["customer_id"] == 642  # return true or false

transactions.loc[transactions["customer_id"] == 642] # return all rows that match with condition

transactions.loc[transactions["customer_id"] == 642, ["customer_id", "sales_cost"]]
# For more than one condition we need to put any condition in paranthesis seperately
transactions.loc[(transactions["customer_id"] == 642) & (transactions["num_items"] > 5)] 
transactions.loc[(transactions["customer_id"] == 642) | (transactions["num_items"] > 5)]

transactions.loc[transactions["customer_id"].isin([642,700])]
transactions.loc[~transactions["customer_id"].isin([642,700])] # Return all except 642 and 700

































