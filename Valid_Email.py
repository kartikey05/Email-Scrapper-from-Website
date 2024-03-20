#2

import csv
import re
import ast
import pandas as pd

def is_valid_email(email):
    # Regular expression for basic email format validation
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email) is not None:
        # Check if there is a digit immediately after the '@' symbol
        if re.search(r"@\d", email):
            return False
        else:
            return True
    else:
        return False

def extract_valid_emails(csv_file):
    valid_emails = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            company_name = row['Company Name']
            emails = ast.literal_eval(row['Emails'])  # Convert string representation of list to actual list
            for email in emails:
                email = email.strip()  # Remove leading/trailing whitespace
                if is_valid_email(email):
                    valid_emails.append({'Company Name': company_name, 'Email': email})
                else:
                    print(f"Ignoring invalid email: {email}")
    return valid_emails

def save_to_csv(data, csv_file):
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    print(f"Valid email addresses saved to {csv_file}")

if __name__ == "__main__":
    input_csv_file = "company_email_addresses2.csv"
    output_csv_file = "valid_email_addresses.csv"

    valid_emails = extract_valid_emails(input_csv_file)
    if valid_emails:
        save_to_csv(valid_emails, output_csv_file)
