import numpy as np
import pandas as pd

df= pd.read_csv('car_selling_price_distribution (1).csv')
print(df.head(10))

print(df.info())
print(df.describe())

print("Average Selling Price:")
print(df['Selling_Price_Lakhs'].mean())

print(df['Price_Bracket'].value_counts())

import matplotlib.pyplot as plt

df['Price_Bracket'].value_counts().plot(kind='bar')

plt.title('Car Selling Price Distribution')
plt.xlabel('Price Bracket')
plt.ylabel('Number of Cars')
plt.show()
