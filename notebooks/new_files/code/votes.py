import csv
import pandas as pd

df = pd.read_csv('cleaned_votes_usa_dataset.csv')

dem_votes = df[['State', 'percent_democrat']]

dem_votes.to_csv('dem_votes.csv', index=False)

print("New CSV file 'dem_votes.csv' created successfully.")