import pandas as pd

def add_jurisdiction(facility_path, facility_chemical_regulatory_info_path):
    # Load the facility.csv file
    facility_df = pd.read_csv(facility_path)

    # Create a mapping from Facility ID to Jurisdiction
    jurisdiction_mapping = facility_df.set_index('Facility ID')['Street Address State'].apply(lambda x: f'STATE_{x}').to_dict()

    # Load the FACILITY_CHEMICAL_REGULATORY_INFORMATION.csv file
    facility_chemical_regulatory_info_df = pd.read_csv(facility_chemical_regulatory_info_path)

    # Add a new column "Jurisdiction" to the DataFrame
    facility_chemical_regulatory_info_df['Jurisdiction'] = facility_chemical_regulatory_info_df['Facility ID'].map(jurisdiction_mapping)

    # Save the updated DataFrame back to the FACILITY_CHEMICAL_REGULATORY_INFORMATION.csv file
    facility_chemical_regulatory_info_df.to_csv(facility_chemical_regulatory_info_path, index=False)

# Example usage
add_jurisdiction('./potamkin/FACILITY.csv', './potamkin/FACILITY_CHEMICAL_REGULATORY_INFORMATION.csv')