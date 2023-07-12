import os
import csv
import sys

# Check if CSV directory and output file arguments are provided
if len(sys.argv) >= 3:
    csv_directory = sys.argv[1]  # CSV directory
    output_file = sys.argv[2]  # Output file path and name
else:
    # If arguments are not provided, use the script's directory as a reference
    script_directory = os.path.dirname(os.path.abspath(__file__))
    csv_directory = script_directory
    output_file = os.path.join(script_directory, 'consolidated_data.csv')

# List to store column headers
headers = []

# List to store all data rows
data_rows = []

# Iterate through all CSV files in the directory
for file in os.listdir(csv_directory):
    if file.endswith('.csv'):
        csv_file = os.path.join(csv_directory, file)
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            current_headers = next(csv_reader)  # Get column headers
            if not headers:
                headers = current_headers
            if current_headers == headers:
                # Add all data rows to data_rows
                data_rows.extend(csv_reader)
            else:
                print(f"The headers of the file '{file}' do not match the previous headers. Skipping the file.")

# Write the consolidated data to a single CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=';')
    csv_writer.writerow(headers)  # Write column headers
    csv_writer.writerows(data_rows)  # Write data rows

print(f"CSV file consolidation completed. The consolidated file has been saved at: {output_file}")
