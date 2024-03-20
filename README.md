
# Email Scrapper from Website 📧

## Description
Email Scrapper from Website is a powerful Python tool designed to extract and validate email addresses from various websites. It utilizes web scraping techniques to collect email addresses and filters out invalid or duplicate entries, providing clean and reliable data for various applications.

## Key Features
- **Web Scraping:** Utilizes Beautiful Soup and Requests libraries for efficient web scraping.
- **Email Validation:** Employs the Email Validator library to validate email addresses.
- **CSV Export:** Saves the extracted and validated email addresses into a CSV file for easy access and analysis.
- **Duplicate Removal:** Removes duplicate email addresses to ensure data accuracy.
- **Special Character Removal:** Filters out email addresses containing special characters after the "@" symbol.

## Technologies Used
- **Python:** A versatile programming language used for the development of the scrapper.
- **Beautiful Soup:** A Python library for pulling data out of HTML and XML files, crucial for web scraping.
- **Requests:** A Python HTTP library used to send HTTP requests, essential for fetching web pages.
- **Email Validator:** A Python library used to validate email addresses with syntax checking, DNS validation, and SMTP validation.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/email-scrapper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd email-scrapper
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Website Traversal Script:**
   - First, traverse the target websites to collect email addresses.
   ```bash
   python traverse_website.py
   ```
2. **Run the Email Validation Script:**
   - Once the traversal is complete, validate the collected email addresses.
   ```bash
   python valid_emails.py
   ```
3. **Run the Duplicate Removal Script:**
   - After validation, remove any duplicate email addresses.
   ```bash
   python remove_duplicate.py
   ```
4. **Run the Special Character Removal Script:**
   - Remove email addresses containing special characters after the "@" symbol.
   ```bash
   python special_Scharacter.py
   ```
5. **Run the Final Email Extraction Script:**
   - Finally, extract the valid email addresses from the processed data.
   ```bash
   python only_emails.py
   ```
6. Follow the on-screen instructions to start each script's execution.

## Example CSV Format
```csv
Company Name,Email
http://www.example1.com/,info@example1.com
http://www.example2.com/,support@example2.com
```

## Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License
This project is licensed under the [MIT License](LICENSE).

## Credits
- Created by [kartikey agarwal](https://github.com/kartikey05)

