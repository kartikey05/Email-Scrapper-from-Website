import pandas as pd

def remove_duplicates(input_csv_file, output_csv_file):
    # Read the input CSV file
    df = pd.read_csv(input_csv_file)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Write the dataframe to the output CSV file
    df.to_csv(output_csv_file, index=False)
    print(f"Duplicate rows removed. Output saved to {output_csv_file}")

if __name__ == "__main__":
    input_csv_file = "valid_email_addresses.csv"
    output_csv_file = "clean_valid_email_addresses.csv"

    remove_duplicates(input_csv_file, output_csv_file)
