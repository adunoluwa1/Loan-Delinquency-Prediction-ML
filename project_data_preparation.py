import pandas as pd

# Importing data
dg = pd.read_csv("dataset_risk_analytics.csv")

# Drop missing values
dg[dg["monthly_income"].isna() == True]
dg.dropna(axis='index',inplace=True)
# print(dg.describe())

# Drop duplicates
dg[dg.duplicated(subset=["loan_id"]) == True]               # Checking for duplicates
dg.drop_duplicates(subset=["loan_id"], inplace=True)        # Droppping duplicates
# dg.describe()


# Wrong format
def conv(x):
    y = []
    for i in x[::2]:
        y.append(int(i))
    return tuple(y)

dg["delq_history"] = dg["delq_history"].apply(conv)

# Convert product to categorical data
dg["product"] = dg["product"].astype('category')
dg["target"] = dg["target"].astype('category')
dg["origination_score_band"] = dg["origination_score_band"].astype('category')

# Final checks for duplicates and null values
dg[dg.duplicated() == True]
dg[dg.duplicated(subset=["loan_id"]) == True]#.info()
# dg

# Reindexing the DataFrame
dg.reset_index(inplace=True, drop=True)    # Reindexing the DF
# print(dg.describe())
# dg.shape

# Analyzing the data
# dg.corr()
print(dg)
dg.info()





