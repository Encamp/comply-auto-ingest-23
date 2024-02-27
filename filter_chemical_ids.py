import pandas as pd

def filter_chemical_ids(file_path, chemical_ids):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Filter rows where 'Chemical ID' is in the list of Chemical IDs
    filtered_df = df[df['Chemical ID'].isin(chemical_ids)]

    # Create the output file path by replacing '.csv' with '_filtered.csv'
    output_path = file_path.replace('.csv', '_filtered.csv')

    # Save the filtered DataFrame to a new CSV file
    filtered_df.to_csv(output_path, index=False)

# List of Chemical IDs to filter
chemical_ids = [
    'f1e18ddb-f06b-4fec-9125-c0f7af1ad31d',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '1267d2d6-b2b0-464d-895b-91eb50feac10',
    '4a2e8b70-e42d-4001-93d8-c0f27be74351',
    '167aa47e-d555-4763-a0af-206522aa7aac',
    '28837094-2a14-4c41-b58c-66d060127d90',
    '5721402c-a444-4084-ba8a-698ae7e2782d',
    'c9c42cc3-3156-462f-8a19-fb8c438ca6f9',
    '9cce1fe6-5e0f-4e75-baba-92dcc56e41fd',
    '6eb2130a-50b8-4989-b279-40cdf431f65c',
]

# Call the function
filter_chemical_ids('./haddad/FACILITY_CHEMICAL_REGULATORY_INFORMATION.csv', chemical_ids)