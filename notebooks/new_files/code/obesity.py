import csv
import pandas as pd

df = pd.read_csv('cleaned_obesity_gdp_dataset.csv')

average_obesity = df.groupby('State')['Adult.Obesity*100', 'Average.Income'].mean().reset_index()

average_obesity.to_csv('average_obesity_by_state.csv', index=False)

print("New CSV file 'average_obesity_by_state.csv' created successfully.")

