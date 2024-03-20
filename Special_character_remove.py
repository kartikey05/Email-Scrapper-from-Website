import csv
import re
import pandas as pd

def remove_special_char_emails(input_csv_file, output_csv_file):
    valid_emails = []
    with open(input_csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        if 'Email' not in reader.fieldnames:
            print("Error: 'Email' column not found in the CSV file.")
            return

        for row in reader:
            company_name = row.get('Company Name', '')  # Safely get the company name
            email = row.get('Email', '')  # Safely get the email
            email = email.strip()  # Remove leading/trailing whitespace
            if not contains_special_character(email):
                valid_emails.append({'Company Name': company_name, 'Email': email})

    if valid_emails:
        save_to_csv(valid_emails, output_csv_file)
    else:
        print("No valid emails found.")

def contains_special_character(email):
    # Regular expression to check if there is any special character after the '@' symbol
    pattern = r"[@][^\w\s]"
    return bool(re.search(pattern, email))

def save_to_csv(data, csv_file):
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    print(f"Filtered emails saved to {csv_file}")

if __name__ == "__main__":
    input_csv_file = "clean_valid_email_addresses.csv"
    output_csv_file = "filtered_valid_email_addresses.csv"

    remove_special_char_emails(input_csv_file, output_csv_file)
