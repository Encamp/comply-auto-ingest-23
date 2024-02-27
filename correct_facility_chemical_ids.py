import pandas as pd
import uuid

def generate_uuid(facility_id, chemical_id):
    # Namespace for UUID generation
    namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')
    return str(uuid.uuid5(namespace, f"{facility_id}-{chemical_id}"))

def correct_facility_chemical_ids(facility_chemical_path, facility_chemical_storage_location_path):
    # Load the datasets
    facility_chemical_df = pd.read_csv(facility_chemical_path)
    facility_chemical_storage_location_df = pd.read_csv(facility_chemical_storage_location_path)

    # Generate unique IDs
    facility_chemical_df['Facility Chemical ID'] = facility_chemical_df.apply(lambda row: generate_uuid(row['Facility ID'], row['Chemical ID']), axis=1)

    # Create a mapping for Facility Chemical IDs
    facility_chemical_mapping = facility_chemical_df.set_index(['Facility ID', 'Chemical ID'])['Facility Chemical ID'].to_dict()

    # Correct the Facility Chemical ID in the storage location dataset
    facility_chemical_storage_location_df['Corrected Facility Chemical ID'] = facility_chemical_storage_location_df.apply(
        lambda row: facility_chemical_mapping.get((row['Facility ID'], row['Facility Chemical ID']), None), axis=1)

    # Replace the original ID with the corrected one
    facility_chemical_storage_location_df['Facility Chemical ID'] = facility_chemical_storage_location_df['Corrected Facility Chemical ID']
    facility_chemical_storage_location_df.drop(columns=['Corrected Facility Chemical ID'], inplace=True)

    # Save the corrected datasets
    corrected_facility_chemical_path = facility_chemical_path.replace('.csv', '_corrected.csv')
    corrected_facility_chemical_storage_location_path = facility_chemical_storage_location_path.replace('.csv', '_corrected.csv')

    facility_chemical_df.to_csv(corrected_facility_chemical_path, index=False)
    facility_chemical_storage_location_df.to_csv(corrected_facility_chemical_storage_location_path, index=False)

    return corrected_facility_chemical_path, corrected_facility_chemical_storage_location_path

# Example usage
corrected_facility_chemical_path, corrected_facility_chemical_storage_location_path = correct_facility_chemical_ids(
    './lexus/FACILITY_CHEMICAL.csv',
    './lexus/FACILITY_CHEMICAL_STORAGE_LOCATION.csv'
)

