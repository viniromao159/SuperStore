#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv("Data/SuperStore - Data.csv")
df.head()

#Sales to float
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
#Bar plot - Top sales per Sub-category

subCategory = (df.groupby(['Sub-Category'])['Order ID'].count()).sort_values(ascending=False).reset_index()

colors = plt.cm.Blues(subCategory['Order ID'])

sns.barplot(x='Order ID',y='Sub-Category', data=subCategory, width=0.7, palette=colors, zorder=3)

plt.title('Top sales per Sub-category', pad=15)

plt.xlabel('Sales count', labelpad=15)

plt.ylabel('Sub-Category', labelpad=15)

plt.grid(axis='x', alpha=0.3, zorder=0)

sns.despine()

# %%
#Line plot - Sales history per month

df["Ship fdate"] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

df["Ship fdate"] = df["Ship fdate"].dt.to_period('M').dt.to_timestamp(how='end')

SalesMonth = (
    df.groupby('Ship fdate')['Sales']
    .sum()
    .reset_index()
    .sort_values(by='Ship fdate')
)

plt.figure(figsize=(9,6))

sns.lineplot(y='Sales', x='Ship fdate', data=SalesMonth)

plt.title('Sales per date')

plt.xlabel('Sales value', labelpad=15)

plt.xticks(rotation=45)

# %%
#Bar plot - Top 10 sales of product

product = (df.groupby(['Product Name'])['Sales'].sum()).nlargest(10).reset_index()

sns.barplot(x='Sales', y='Product Name', data=product, width=0.7, zorder=3)

plt.title('Top 10 sales of product', pad=15)

plt.xlabel('Sales count', labelpad=15)

plt.ylabel('Sub-Category', labelpad=15)

plt.grid(axis='x', alpha=0.3, zorder=0)

sns.despine()

# %%
#Bar plot - Top sales per City

City = (df.groupby(['City'])['Order ID'].count()).nlargest(10).reset_index()

sns.barplot(x='Order ID', y='City', data=City, width=0.7, zorder=3)

plt.title('Top sales per City', pad=15)

plt.xlabel('Sales count', labelpad=15)

plt.ylabel('Sub-Category', labelpad=15)

plt.grid(axis='x', alpha=0.3, zorder=0)

sns.despine()


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
region = (df.groupby(['Region'])['Order ID'].count()).reset_index()
plot = sns.barplot(y='Order ID',x='Region', data=region)
plot.set_title('Top sales per Region')
plot.set_xlabel('Sales count')