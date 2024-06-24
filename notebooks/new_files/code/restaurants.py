import csv
import pandas as pd

df = pd.read_csv('cleaned_restaurants_dataset.csv')

average_obesity = df[['State', 'All fast food restaurants']]

df_sorted = df.sort_values(by='State')

average_obesity.to_csv('restaurants_state.csv', index=False)

print("New CSV file 'restaurants_state.csv' created successfully.")