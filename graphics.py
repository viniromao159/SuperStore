#%%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/SuperStore - Data.csv")
df.head()
# %%

sales_description = df["Sales"].replace('$','', regex=True).str.replace(",", ".", regex=True).astype(float)
sales_description.describe()
# %%
