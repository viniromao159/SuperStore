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
df["Ship month-year"] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

df["Ship month-year"] = sorted(df["Ship month-year"])

df["Ship month-year"] = df["Ship month-year"].dt.strftime('%m/%Y')

df["Ship month-year"].reset_index()

df_data = df[["Ship month-year",'Sales']] 

df_data = df_data.sort_values(by="Ship month-year")

SalesMonth = df_data.groupby(by='Ship month-year', group_keys=True)[['Sales']].sum()

SalesMonth

# plt.figure(figsize=(10,4))

# sns.lineplot(y='Sales', x='Ship month-year', data=SalesMonth)

# plt.title('Sales per date')

# plt.xlabel('Sales value', labelpad=15)

# plt.xticks(rotation=45)
# %%
