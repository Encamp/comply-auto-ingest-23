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
    '0d91a056-94c2-4a07-9862-f7c366db46bb',
    '3573bf4e-77b8-46b4-971e-aa090e66f76e',
    '70d0d831-2d96-47d2-aae8-a4e3530419dc',
    '60f82f3a-1e3b-4ce2-a7a6-943026e1df22',
    '9c76f016-1c79-4dee-b31a-abd98eb91d0c',
    '70d0d831-2d96-47d2-aae8-a4e3530419dc',
    '60f82f3a-1e3b-4ce2-a7a6-943026e1df22',
    '9c76f016-1c79-4dee-b31a-abd98eb91d0c',
    '70d0d831-2d96-47d2-aae8-a4e3530419dc',
    '60f82f3a-1e3b-4ce2-a7a6-943026e1df22',
    '9c76f016-1c79-4dee-b31a-abd98eb91d0c',
    '70d0d831-2d96-47d2-aae8-a4e3530419dc',
    '60f82f3a-1e3b-4ce2-a7a6-943026e1df22',
    '9c76f016-1c79-4dee-b31a-abd98eb91d0c',
    '70d0d831-2d96-47d2-aae8-a4e3530419dc',
    '60f82f3a-1e3b-4ce2-a7a6-943026e1df22',
    '9c76f016-1c79-4dee-b31a-abd98eb91d0c',
    '70d0d831-2d96-47d2-aae8-a4e3530419dc',
    '60f82f3a-1e3b-4ce2-a7a6-943026e1df22',
    '9c76f016-1c79-4dee-b31a-abd98eb91d0c',
    '70d0d831-2d96-47d2-aae8-a4e3530419dc',
    '60f82f3a-1e3b-4ce2-a7a6-943026e1df22',
    '9c76f016-1c79-4dee-b31a-abd98eb91d0c',
]


# Call the function
filter_chemical_ids('./potamkin/FACILITY_CHEMICAL_REGULATORY_INFORMATION.csv', chemical_ids)
