import os
import pandas as pd
import csv

data_root = r'/home/sridhar/DeepBlocker_data_emb/data/Structured/Amazon-Google'
save_root = r'/home/sridhar/ditto/DeepBlocker_v1/data'

#read train, val, test csvs and concatenate them in a single file

# Read the first CSV file with header
df1 = pd.read_csv(os.path.join(data_root,'train.csv'))
df2 = pd.read_csv(os.path.join(data_root,'valid.csv'))
df3 = pd.read_csv(os.path.join(data_root,'test.csv'))

df1 = df1[df1['label'] == 1]
df2 = df2[df2['label'] == 1]
df3 = df3[df3['label'] == 1]

# Concatenate all dataframes
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Keep only 'ltable_id' and 'rtable_id' columns
combined_df = combined_df[['ltable_id', 'rtable_id']]

# Write the combined dataframe to a new CSV file
combined_df.to_csv('matches1.csv', index=False)


