import pandas as pd
import sys

def convert_units(row):
    conversion_factors = {'QUARTS': 0.25, 'OUNCES': 1/128}
    units_to_convert = ['QUARTS', 'OUNCES']

    for column in ['Max Amount', 'Average Amount', 'Max Amount Largest Container']:
        if row['Unit'] in units_to_convert:
            row[column] = row[column] * conversion_factors[row['Unit']]
    if row['Unit'] in units_to_convert:
        row['Unit'] = 'GALLONS'
    return row

def fill_missing_values(df):
    for index, row in df.iterrows():
        max_amount = row['Max Amount']
        average_amount = row['Average Amount']
        max_amount_largest_container = row['Max Amount Largest Container']

        if pd.notnull(max_amount):
            if pd.isnull(average_amount):
                df.at[index, 'Average Amount'] = max_amount
            if pd.isnull(max_amount_largest_container):
                df.at[index, 'Max Amount Largest Container'] = max_amount
        elif pd.notnull(average_amount):
            if pd.isnull(max_amount):
                df.at[index, 'Max Amount'] = average_amount
            if pd.isnull(max_amount_largest_container):
                df.at[index, 'Max Amount Largest Container'] = average_amount
        elif pd.notnull(max_amount_largest_container):
            if pd.isnull(max_amount):
                df.at[index, 'Max Amount'] = max_amount_largest_container
            if pd.isnull(average_amount):
                df.at[index, 'Average Amount'] = max_amount_largest_container
        
        # Fill remaining nulls with 0
        df.fillna(0, inplace=True)

    return df

def process_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Fill missing values according to the rules
    df = fill_missing_values(df)

    # Convert units and amounts
    df = df.apply(convert_units, axis=1)

    # Write the transformed DataFrame to stdout
    df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    process_csv(file_path)
