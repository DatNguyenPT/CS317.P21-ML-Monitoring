import pandas as pd

# Define the data path
data_path = "MLFlow/data"  # adjust this path according to your data location

# Read the parquet file
df_1 = pd.read_parquet(f'{data_path}/Benign-Monday-no-metadata.parquet')

# Print original shape
print("Original shape:", df_1.shape)

# Remove the first row (you can modify the index as needed)
df_1 = df_1.drop(index=0)

# Print new shape to confirm removal
print("New shape after removing one row:", df_1.shape)

# Save the modified dataframe 
df_1.to_parquet(f'{data_path}/Benign-Monday-no-metadata-modified.parquet')