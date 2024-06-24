import pandas as pd

df1 = pd.read_csv('average_obesity_by_state.csv')
df2 = pd.read_csv('dem_votes.csv')
df3 = pd.read_csv('restaurants_state.csv')
df4 = pd.read_csv('unemployment_by_state.csv')
df5 = pd.read_csv('education_by_state.csv')

merged_df = pd.merge(df1, df2, on='State')
merged_df = pd.merge(merged_df, df3, on='State')
merged_df = pd.merge(merged_df, df4, on='State')
merged_df = pd.merge(merged_df, df5, on='State')

merged_df.to_csv('combined_file.csv', index=False)
