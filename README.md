# Rezerva Loc - BCU Automation

This repository contains a Python script that automates the reservation process for a specific location using Selenium WebDriver. The script logs into the BCU system, searches for available locations, reserves one, and sends an email confirmation.

## Prerequisites

Before running the script, ensure you have the following:

1. Python 3.x installed.
2. Google Chrome installed.
3. ChromeDriver installed and placed in a specific path (`E:\\chromedriver-win64\\chromedriver.exe` in this case).
4. Required Python packages installed:
   - `selenium`
   - `smtplib`
   - `email`

## Setup

### Install Python Packages

You can install the required packages using `pip`:

```bash
pip install selenium
```

### ChromeDriver

Download ChromeDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the specified path or update the script to the path where you have ChromeDriver.

## Configuration

### Email Credentials

Update the email credentials in the `send_email` function:

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"
RECIPIENT_EMAIL = "recipient_email@example.com"
```

### Library Credentials

Update the login credentials in the `rezerva_loc` function:

```python
txtBarcod.send_keys("YourBarcode")
txtParola.send_keys("YourPassword")
```

## Running the Script

Run the script using Python:

```bash
python rezerva_loc.py
```

The script will:

1. Open Chrome and navigate to the BCU login page.
2. Log in using the provided credentials.
3. Search for available locations.
4. Reserve the first available location.
5. Send an email confirmation with the reserved location details.

## Error Handling

The script includes error handling for common issues such as timeouts and missing elements. If a step fails, the script will retry up to 10 times before giving up.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have any suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

## Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- [Python](https://www.python.org/)

---

Feel free to customize this README to better fit your project and provide any additional information that might be helpful to users or contributors.
