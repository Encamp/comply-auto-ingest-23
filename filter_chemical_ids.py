import pandas as pd

def filter_chemical_ids(file_path, chemical_ids):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Filter rows where 'Chemical ID' is in the list of Chemical IDs
    filtered_df = df[~df['Chemical ID'].isin(chemical_ids)]

    # Create the output file path by replacing '.csv' with '_filtered.csv'
    output_path = file_path.replace('.csv', '_filtered.csv')

    # Save the filtered DataFrame to a new CSV file
    filtered_df.to_csv(output_path, index=False)

# List of Chemical IDs to filter
chemical_ids = [
    '5e81e2e0-d60d-4ffb-856a-c3317361f15f',
    '6320a1e3-f459-4306-8d1d-7139b18893bf',
    'b1cde203-6b39-49f5-b3a0-66ff356e3785',
    'beb05719-235b-42fc-b535-44548ec9d144',
    'd11cbdf3-7a8d-403b-8f59-04e578f137c0',
    'd9bd936e-b8e1-46b1-b01f-aa12484b0349',
    '5e81e2e0-d60d-4ffb-856a-c3317361f15f',
    '6320a1e3-f459-4306-8d1d-7139b18893bf',
    'b1cde203-6b39-49f5-b3a0-66ff356e3785',
    'beb05719-235b-42fc-b535-44548ec9d144',
    'd11cbdf3-7a8d-403b-8f59-04e578f137c0',
    'd9bd936e-b8e1-46b1-b01f-aa12484b0349',
    '5e81e2e0-d60d-4ffb-856a-c3317361f15f',
    '6320a1e3-f459-4306-8d1d-7139b18893bf',
    'b1cde203-6b39-49f5-b3a0-66ff356e3785',
    'beb05719-235b-42fc-b535-44548ec9d144',
    'd11cbdf3-7a8d-403b-8f59-04e578f137c0',
    'd9bd936e-b8e1-46b1-b01f-aa12484b0349',
    '5e81e2e0-d60d-4ffb-856a-c3317361f15f',
    '6320a1e3-f459-4306-8d1d-7139b18893bf',
    'b1cde203-6b39-49f5-b3a0-66ff356e3785',
    'beb05719-235b-42fc-b535-44548ec9d144',
    'd11cbdf3-7a8d-403b-8f59-04e578f137c0',
    'd9bd936e-b8e1-46b1-b01f-aa12484b0349',
    '5e81e2e0-d60d-4ffb-856a-c3317361f15f',
    '6320a1e3-f459-4306-8d1d-7139b18893bf',
    'b1cde203-6b39-49f5-b3a0-66ff356e3785',
    'beb05719-235b-42fc-b535-44548ec9d144',
    'd11cbdf3-7a8d-403b-8f59-04e578f137c0',
    'd9bd936e-b8e1-46b1-b01f-aa12484b0349',
    '5e81e2e0-d60d-4ffb-856a-c3317361f15f',
    '6320a1e3-f459-4306-8d1d-7139b18893bf',
    'b1cde203-6b39-49f5-b3a0-66ff356e3785',
    'beb05719-235b-42fc-b535-44548ec9d144',
    'd11cbdf3-7a8d-403b-8f59-04e578f137c0',
    'd9bd936e-b8e1-46b1-b01f-aa12484b0349',
    '5e81e2e0-d60d-4ffb-856a-c3317361f15f',
    '6320a1e3-f459-4306-8d1d-7139b18893bf',
    'b1cde203-6b39-49f5-b3a0-66ff356e3785',
    'beb05719-235b-42fc-b535-44548ec9d144',
    'd11cbdf3-7a8d-403b-8f59-04e578f137c0',
    'd9bd936e-b8e1-46b1-b01f-aa12484b0349',
]

# Call the function
filter_chemical_ids('./lexus/FACILITY_CHEMICAL_REGULATORY_INFORMATION.csv', chemical_ids)