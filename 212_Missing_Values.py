
################################################
# Pandas - Missing Values
################################################

import pandas as pd

customer_details = pd.read_excel("grocery_database.xlsx", sheet_name = "customer_details") 
customer_details.shape # (870, 4)

customer_details.isna().sum()
customer_details.notna().sum()


customer_details["distance_from_store"].isna().sum()


customer_details[customer_details["distance_from_store"].isna()]
"""
     customer_id  distance_from_store gender  credit_score
169          517                  NaN    NaN           NaN
314          105                  NaN      F          0.71
466          218                  NaN      M          0.37
576          362                  NaN    NaN          0.56
845          292                  NaN    NaN           NaN
"""

# Get all rows without having null in distance_from_store columns
customer_details[customer_details["distance_from_store"].notna()] 




customer_details.dropna(how = "any") # remove row with even one nan value
customer_details.dropna(how = "all") # remove row when all values are nan 

customer_details.dropna(how = "any", subset = ["distance_from_store"])
customer_details.dropna(how = "any", subset = ["distance_from_store", "gender"])


import numpy as np
my_df = pd.DataFrame({"A": [1,2,4,np.nan,5,np.nan,7],
                      "B": [4,np.nan,7,np.nan,1,np.nan,2]})



my_df["A"].fillna(value = 0)
impute_value = my_df["A"].mean()
my_df["A"].fillna(value = impute_value)


customer_details.isna().sum()
customer_details["gender"].fillna(value = "U", inplace = True)

customer_details["gender"].value_counts()
"""
gender
F    485
M    380
U      5
Name: count, dtype: int64

"""


customer_details["distance_from_store"].describe()
customer_details["distance_from_store"].fillna(value = customer_details["distance_from_store"].median(), inplace = True)









































