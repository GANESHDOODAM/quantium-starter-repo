import pandas as pd
import os

# Define file paths
data_folder = "data"  # Folder where your CSV files are located
files = ["/Users/ganeshdoodam/PycharmProjects/quantium-starter-repo/data/daily_sales_data_0.csv", "/Users/ganeshdoodam/PycharmProjects/quantium-starter-repo/data/daily_sales_data_1.csv", "/Users/ganeshdoodam/PycharmProjects/quantium-starter-repo/data/daily_sales_data_2.csv"]  # Replace with actual file names
file_paths = [os.path.join(data_folder, file) for file in files]

# Initialize an empty list to store dataframes
dataframes = []

# Process each file
for file in file_paths:
    df = pd.read_csv(file)

    # Filter only Pink Morsels
    df = df[df["product"] == "Pink Morsels"]

    # Compute sales column
    df["sales"] = df["quantity"] * df["price"]

    # Select required columns
    df = df[["sales", "date", "region"]]

    # Append to the list
    dataframes.append(df)

# Combine all dataframes
final_df = pd.concat(dataframes, ignore_index=True)

# Save to CSV
output_file = "formatted_sales.csv"
final_df.to_csv(output_file, index=False)

print(f"Formatted file saved as {output_file}")
