import pandas as pd

def correct_chemical_ids(chemicals_path, components_path):
    # Load the datasets with "N/A" as a string to be kept as is
    chemicals_df = pd.read_csv(chemicals_path, keep_default_na=False, na_values=[''])
    components_df = pd.read_csv(components_path, keep_default_na=False, na_values=[''])

    # Identify duplicates in the chemicals dataset
    duplicates = chemicals_df[chemicals_df.duplicated('Chemical ID', keep=False)]

    # Remove duplicates from the chemicals dataset
    chemicals_df.drop_duplicates('Chemical ID', keep='first', inplace=True)

    # Identify and remove duplicates in the components dataset based on 'Chemical ID' and 'Name'
    components_df.drop_duplicates(subset=['Chemical ID', 'Name'], keep='first', inplace=True)

    # Convert boolean columns to string
    for col in chemicals_df.select_dtypes(include=['bool']).columns:
        chemicals_df[col] = chemicals_df[col].apply(lambda x: 'TRUE' if x else 'FALSE')
    for col in components_df.select_dtypes(include=['bool']).columns:
        components_df[col] = components_df[col].apply(lambda x: 'TRUE' if x else 'FALSE')

    # Save the corrected datasets
    corrected_chemicals_path = chemicals_path.replace('.csv', '_corrected.csv')
    corrected_components_path = components_path.replace('.csv', '_corrected.csv')
    chemicals_df.to_csv(corrected_chemicals_path, index=False)
    components_df.to_csv(corrected_components_path, index=False)

    return corrected_chemicals_path, corrected_components_path


corrected_chemicals_path, corrected_components_path = correct_chemical_ids(
    './lexus/CHEMICALS-chemicals.csv',
    './lexus/CHEMICALS-components.csv'
)
