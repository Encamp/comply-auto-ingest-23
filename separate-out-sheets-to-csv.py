import os
import sys
import pandas as pd

def xlsx_to_csv(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".xlsx"):
                file_path = os.path.join(root, file)
                # Read the Excel file
                xls = pd.ExcelFile(file_path)
                # Get the base name without extension for naming the CSV files
                base_name = os.path.splitext(file)[0]
                for sheet_name in xls.sheet_names:
                    # Read each sheet into a pandas DataFrame
                    df = pd.read_excel(file_path, sheet_name=sheet_name)
                    # Construct the CSV file name
                    csv_file_name = f"{root}/{base_name}_{sheet_name}.csv"
                    # Save the DataFrame to CSV
                    df.to_csv(csv_file_name, index=False)
                    print(f"Saved {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <root_directory>")
        sys.exit(1)
    root_directory = sys.argv[1]
    xlsx_to_csv(root_directory)
