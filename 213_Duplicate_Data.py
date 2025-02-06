
################################################
# Pandas - Dealing with Duplicate Data
################################################

import pandas as pd

my_df = pd.DataFrame({"customer_id": [1,1,2,2,3],
                      "transaction_id": [101,102,103,103,104]})


my_df.duplicated()
my_df.duplicated().sum()


my_df["customer_id"].duplicated()

my_df[my_df.duplicated()] # return duplicated row

my_df.duplicated(keep = "first") # default - keep first and consider second  as a duplicated
my_df.duplicated(keep = "last")  # keep last and consider first as a duplicated
my_df.duplicated(keep = False)   # consider all of them as duplicated


my_df.drop_duplicates()