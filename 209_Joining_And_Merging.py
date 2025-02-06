

#######################################
# Pandas - Joining & Merging DataFrames
#######################################

import pandas as pd
transactions =pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")


# JOINING

df_a = pd.DataFrame({"A": [1,2,3], "B": [4,5,6]})
df_b = pd.DataFrame({"C": [1,2,3], "D": [4,5,6]})

df_c = pd.concat([df_a, df_b], axis = 1)

# ? not a good result => if we want to concat (put top of each other), we need to have the same column names
df_c = pd.concat([df_a, df_b], axis = 0) 

df_a = pd.DataFrame({"A": [1,2,3], "B": [4,5,6]})
df_b = pd.DataFrame({"A": [1,2,3], "B": [4,5,6]})
df_c = pd.concat([df_a, df_b], axis = 0)


# MERGING

df_a = pd.DataFrame({"user_id": [1,2,3,5,7], "age": [41,15,60,18,29]})
df_b = pd.DataFrame({"user_id": [1,2,3,4,5], "gender": ["m","f","f","f","m"]})


# INNER JOIN

pd.merge(df_a, df_b, how = "inner", on = "user_id")


# LEFT JOIN AND RIGHT JOIN

pd.merge(df_a, df_b, how = "left", on = "user_id")
pd.merge(df_a, df_b, how = "right", on = "user_id")


# OUTER JOIN = left & right join

pd.merge(df_a, df_b, how = "outer", on = "user_id")


# JOIN ON MULTIPLE COLUMNS
pd.merge(df_a, df_b, how = "outer", on = ["user_id", "column2"])


# Join when we do not hace similar column names
df_b.rename(columns = {"user_id" : "customer_id"}, inplace = True)


pd.merge(df_a, df_b, how = "inner", left_on = "user_id", right_on = "customer_id")

























