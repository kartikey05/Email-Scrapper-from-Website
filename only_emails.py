# 5

import csv

def read_emails_from_csv(csv_file):
    emails = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            emails.append(row['Email'])
    return emails

def save_to_csv(data, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Email'])  # Write header
        for email in data:
            writer.writerow([email])

if __name__ == "__main__":
    input_csv_file = "filtered_valid_email_addresses.csv"
    output_csv_file = "emails_list.csv"

    emails = read_emails_from_csv(input_csv_file)
    if emails:
        save_to_csv(emails, output_csv_file)
        print(f"Emails saved to {output_csv_file}")
    else:
        print("No emails found.")
