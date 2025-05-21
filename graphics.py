#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Data/SuperStore - Data.csv")
df.head()

#Converter sales para float
df['Sales'] = (
    df['Sales']
    .astype(str)
    .str.replace(r'[R$\s]', '', regex=True)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
    .str.replace(r'[^\d.-]', '', regex=True)
    .astype(float)
)

# %%
subCategory = (df.groupby(['Sub-Category'])['Order ID'].count()).sort_values(ascending=False).reset_index()
plot = sns.barplot(x='Order ID',y='Sub-Category', data=subCategory)
plot.set_title('Top sales per Sub-category')
plot.set_xlabel('Sales count')

# %%
region = (df.groupby(['Region'])['Order ID'].count()).reset_index()
plot = sns.barplot(y='Order ID',x='Region', data=region)
plot.set_title('Top sales per Region')
plot.set_xlabel('Sales count')

# %%
product = (df.groupby(['Product Name'])['Sales'].sum()).nlargest(10).reset_index()
plot = sns.barplot(x='Sales', y='Product Name', data=product)
plot.set_title('Top sales per Product Name')
plot.set_xlabel('Sales count')

# %%
City = (df.groupby(['City'])['Order ID'].count()).nlargest(10).reset_index()
plot = sns.barplot(x='Order ID', y='City', data=City)
plot.set_title('Top sales per City')
plot.set_xlabel('Sales count')

# %%
Customer_Name = (df.groupby(['Customer Name'])['Order ID'].count()).nlargest(10).reset_index()
plot = sns.barplot(x='Order ID', y='Customer Name', data=Customer_Name)
plot.set_title('Top sales per Customer Name')
plot.set_xlabel('Sales count')

# %%
Segment = (df.groupby(['Segment'])['Order ID'].count()).reset_index()
plot = sns.barplot(y='Order ID', x='Segment', data=Segment)
plot.set_title('Top sales per Segment')
plot.set_xlabel('Sales count')

# %%
