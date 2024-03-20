# import csv
# import requests
# import re
# from bs4 import BeautifulSoup
# import pandas as pd

# def extract_emails(html_content):
#     """
#     Extracts email addresses from HTML content.
#     """
#     # Regular expression to match email addresses
#     email_pattern = r'[\w\.-]+@[\w\.-]+'

#     # Find email addresses in the HTML content
#     emails = re.findall(email_pattern, html_content)

#     return emails

# def traverse_websites(csv_file):
#     emails = []
#     with open(csv_file, 'r', newline='', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             url = row['company_name'].strip()  # Accessing 'company_name' column
#             print(f"Accessing URL: {url}")  # Debug print statement
#             try:
#                 response = requests.get(url)
#                 if response.status_code == 200:
#                     html_content = response.text
#                     extracted_emails = extract_emails(html_content)
#                     emails.extend(extracted_emails)
#                     print(f"Found {len(extracted_emails)} email(s) on {url}")
#                 else:
#                     print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
#             except Exception as e:
#                 print(f"Error accessing {url}: {str(e)}")

#     return emails

# def save_to_csv(data, csv_file):
#     """
#     Save extracted email addresses to a CSV file.
#     """
#     df = pd.DataFrame(data, columns=['Emails'])
#     df.to_csv(csv_file, index=False)
#     print(f"Email addresses saved to {csv_file}")

# if __name__ == "__main__":
#     csv_file = "company_Website.csv"
#     emails = traverse_websites(csv_file)
#     if emails:
#         save_to_csv(emails, "email_addresses.csv")



import csv
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

def extract_emails(html_content):
    """
    Extracts email addresses from HTML content.
    """
    # Regular expression to match email addresses
    email_pattern = r'[\w\.-]+@[\w\.-]+'

    # Find email addresses in the HTML content
    emails = re.findall(email_pattern, html_content)

    return emails

def traverse_websites(csv_file):
    company_emails = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            company_name = row['company_name'].strip()  # Accessing 'company_name' column
            url = row['company_name'].strip()  # Assuming the URL is the same as company name
            print(f"Accessing URL: {url}")  # Debug print statement
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    html_content = response.text
                    extracted_emails = extract_emails(html_content)
                    if extracted_emails:
                        company_emails.append({'Company Name': company_name, 'Emails': extracted_emails})
                        print(f"Found {len(extracted_emails)} email(s) for {company_name}")
                    else:
                        print(f"No email addresses found for {company_name}")
                else:
                    print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error accessing {url}: {str(e)}")

    return company_emails

def save_to_csv(data, csv_file):
    """
    Save company names and corresponding email addresses to a CSV file.
    """
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Company Name', 'Emails'])
        writer.writeheader()
        for item in data:
            writer.writerow(item)
    print(f"Company names and corresponding email addresses saved to {csv_file}")

if __name__ == "__main__":
    csv_file = "company_Website.csv"
    company_emails = traverse_websites(csv_file)
    if company_emails:
        save_to_csv(company_emails, "company_email_addresses2.csv")
