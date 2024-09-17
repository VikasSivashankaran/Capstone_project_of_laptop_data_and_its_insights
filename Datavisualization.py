import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


url = 'laptops_data.csv'
data = pd.read_csv(url)

data['Price'] = data['Price'].replace('[\$,]', '', regex=True).astype(float)  
data['Rating'] = data['Rating'].astype(int)

plt.figure(figsize=(10, 6))
plt.hist(data['Rating'], bins=range(1, 6), edgecolor='black')
plt.title('Histogram of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.xticks(range(1, 6))
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data['Rating'], data['Price'], alpha=0.7)
plt.title('Scatter Plot of Price vs Rating')
plt.xlabel('Rating')
plt.ylabel('Price')
plt.grid(True)
plt.show()


fig, axs = plt.subplots(1, 2, figsize=(14, 6))

axs[0].hist(data['Rating'], bins=range(1, 6), edgecolor='black')
axs[0].set_title('Histogram of Ratings')
axs[0].set_xlabel('Rating')
axs[0].set_ylabel('Frequency')
axs[0].set_xticks(range(1, 6))
axs[0].grid(True)

scatter = axs[1].scatter(data['Rating'], data['Price'], alpha=0.7)
axs[1].set_title('Scatter Plot of Price vs Rating')
axs[1].set_xlabel('Rating')
axs[1].set_ylabel('Price')
axs[1].grid(True)

plt.tight_layout()
plt.show()

avg_price_by_rating = data.groupby('Rating')['Price'].mean()
plt.figure(figsize=(10, 6))
avg_price_by_rating.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Price by Rating')
plt.xlabel('Rating')
plt.ylabel('Average Price')
plt.xticks(range(len(avg_price_by_rating.index)), avg_price_by_rating.index)
plt.grid(axis='y')
plt.show()

rating_counts = data['Rating'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(rating_counts))))
plt.title('Distribution of Ratings')
plt.show()



df = pd.read_csv('laptops_data.csv')

fig = px.line_3d(df, x="Device Name", y="Rating", z="Price")

fig.show()


fig = px.scatter_3d(df,x="Device Name", y="Rating", z="Price", color='Price',
                    size='Rating', symbol='Rating')

fig.show()

fig = px.bar(df, x='Rating', y="Price")

fig.show()


df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float) 
df['Price_Bins'] = pd.cut(df['Price'], bins=10)  # Group prices into 10 bins

fig = px.bar(df, x="Device Name", y="Rating", color='Price_Bins',
             facet_row='Rating', facet_col='Price_Bins', 
             facet_col_spacing=0.01)
fig.show()

fig = px.box(df, x="Rating", y="Price")

fig.show()


fig = px.box(df,x="Device Name", y="Rating", color='Price',
             facet_row='Rating', boxmode='group',
             notched=True)

fig.show()
print(fig)

fig = px.histogram(df, x="Price")
fig = px.histogram(df, x="Rating", color='Price',
                   nbins=50, histnorm='percent',
                   barmode='overlay')
fig.show()

fig = px.violin(df, x="Rating", y="Price")
fig = px.violin(df, x="Rating", y="Price", color='Device Name',
                facet_row='Rating', box=True)
fig.show()

fig = px.pie(df, values="Rating", names="Price")
fig = px.pie(df, values="Rating", names="Device Name",
             color_discrete_sequence=px.colors.sequential.RdBu,
             opacity=0.7, hole=0.5)
fig.show()