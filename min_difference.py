import pandas as pd

def add_min_date_difference(df):
    """
    Adds a new column 'MinDateDifference' to the DataFrame, storing the minimum difference in days
    between the current row and any other row with the same ID.

    Args:
        df (pandas.DataFrame): Input DataFrame with 'ID' and 'Date' columns.

    Returns:
        pandas.DataFrame: DataFrame with the additional 'MinDateDifference' column.
    """
    df['MinDateDifference'] = None
    
    for id_value in df['ID'].unique():
        filtered_df = df[df['ID'] == id_value]
        num_rows = len(filtered_df)
        
        if num_rows == 1:
            continue
        
        sorted_dates = filtered_df['Date'].sort_values()
        date_diff = (sorted_dates - sorted_dates.shift()).dropna()
        min_diff = date_diff.min().days
        
        # Update the 'MinDateDifference' column for rows with the same ID
        df.loc[df['ID'] == id_value, 'MinDateDifference'] = min_diff
    
    return df

# Import dataset from Excel file
df = pd.read_excel("ToyData.xlsx")

# Add the 'MinDateDifference' column to the DataFrame
df_with_min_diff = add_min_date_difference(df)

# Write the updated DataFrame to a new Excel file
df_with_min_diff.to_excel("dataset_with_min_diff.xlsx", index=False)

def group_by_id(df):
    grouped_df = df.groupby('ID')['MinDateDifference'].apply(list).reset_index(name='GroupedDifferences')
    return grouped_df

import pandas as pd

def get_min_by_id(df):
    """
    Returns the minimum value of the 'MinDateDifference' column for each unique ID.

    Args:
        df (pandas.DataFrame): Input DataFrame with 'ID' and 'MinDateDifference' columns.

    Returns:
        pandas.DataFrame: DataFrame with the minimum difference for each unique ID.
                          Columns: 'ID' - unique ID values, 'MinDifference' - minimum difference.
    """
    grouped_df = df.groupby('ID')['MinDateDifference'].min().reset_index(name='MinDifference')
    return grouped_df

# Example usage
# Assuming you have a dataframe named 'df_with_min_diff' with columns 'ID', 'Date', and 'MinDateDifference'
# Import dataset from Excel file
df = pd.read_excel("dataset_with_min_diff.xlsx")


# Get the minimum difference for each ID
min_diff_df = get_min_by_id(df_with_min_diff)

# Display the DataFrame with the minimum differences as rows
print(df_with_min_diff)

# Display the DataFrame with the minimum differences
print(min_diff_df)
