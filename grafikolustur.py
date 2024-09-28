import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('housing_1.csv',  skipinitialspace=True)

df.columns = df.columns.str.strip()
print(df.columns)

renkler=("red", "green", "blue", "orange", "purple", "yellow") 

#area vs price
plt.figure(figsize=(10,6))
plt.scatter(df['area'], df['price'], color='red')
plt.title('Price vs Area')
plt.xlabel('Area (sq ft)')
plt.ylabel('price (in currency)')
plt.grid(True)
plt.show()

#ibedrooms vs price
plt.figure(figsize=(10,6))
plt.scatter(df['bedrooms'], df['price'], color='blue')
plt.title('Number of Bedrooms vs Price')
plt.xlabel('Number of Bedrooms (sq ft)')
plt.ylabel('price (in currency)')
plt.xticks(range(1, len(df['bedrooms'].unique()) + 1), df['bedrooms'].unique())
plt.grid(True)
plt.show()

#stories vs price
plt.figure(figsize=(10,6))
plt.scatter(df['stories'], df['price'], color='purple')
plt.title('Stories vs Price')
plt.xlabel('Stories (sq ft)')
plt.ylabel('price (in currency)')
plt.xticks(range(1, len(df['stories'].unique()) + 1), df['stories'].unique())
plt.grid(True)
plt.show()

#'bathrooms' ve 'furnishing status' için ortalama fiyat hesaplama
mean_price_by_bathrooms = df.groupby('bathrooms')['price'].mean().reset_index()

df['furnishing_status'] = df['furnishing_status'].str.strip()
print(df['furnishing_status'].unique())


mean_price_by_furnishing_status = df.groupby('furnishing_status')['price'].mean().reset_index()

#'bathrooms' sayısına göre ortalama fiyatlar
plt.figure(figsize=(10,6))
plt.bar(mean_price_by_bathrooms['bathrooms'].astype(str), mean_price_by_bathrooms['price'], color= 'pink')
plt.title('Average Price by Number of Bathrooms')
plt.xlabel('Number of Bathrooms')
plt.ylabel('Average Price (in currency)')
plt.grid(axis='y')
plt.show()

#'furnishins_status'a göre ortalama fiyatlar
plt.figure(figsize=(10,6))
plt.bar(mean_price_by_furnishing_status['furnishing_status'], mean_price_by_furnishing_status['price'], color= 'green')
plt.title('Average Price by Furnishing Status')
plt.xlabel('Furnishing Status')
plt.ylabel('Average Price (in currency)')
plt.grid(axis='y')
plt.show()

#sayısal sütunlar
no_columns= ['price', 'area', 'bedrooms', 'bathrooms', 'stories']

#korelasyon matrisi hesaplama
correlation_matrix = df[no_columns].corr()
print(correlation_matrix)

#görselleştirme
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=1)
plt.title('Korelasyon Matrisi')
plt.show()