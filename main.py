import pandas as pd
import numpy as np

# Load the three datasets
df_2023 = pd.read_csv('PLACES__Local_Data_for_Better_Health,_County_Data_2023_release_20251206.csv')
df_2024 = pd.read_csv('PLACES__Local_Data_for_Better_Health,_County_Data_2024_release_20251206.csv')
df_2025 = pd.read_csv('PLACES__Local_Data_for_Better_Health,_County_Data,_2025_release_20251206.csv')

# Add a year column to each dataset for tracking
df_2023['year'] = 2023
df_2024['year'] = 2024
df_2025['year'] = 2025

# Merge the datasets vertically (stacking rows)
df_merged = pd.concat([df_2023, df_2024, df_2025], ignore_index=True)

# Basic cleaning operations
# 1. Remove duplicates
df_merged = df_merged.drop_duplicates()

# 2. Handle missing values
df_merged = df_merged.dropna()  # Or use fillna() to fill with specific values

# 3. Check data types
print(df_merged.dtypes)

# 4. Basic statistics
print(df_merged.describe())

# Save the cleaned and merged dataset
df_merged.to_csv('merged_cleaned_data.csv', index=False)