# Pytest Selenium Automation Framework

A scalable Selenium Automation Framework built using Python, Pytest and Page Object Model (POM).

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- HTML Reports
- Logging
- Excel Data Handling
- Configuration File
- WebDriver Manager

---

## Project Structure

```
pytest-selenium-framework/
│
├── Configuration/
│   └── config.ini
│
├── Logs/
│   └── log_file.log
│
├── Reports/
│   └── report.html
│
├── Screenshots/
│
├── TestData/
│   └── test_data.xlsx
│
├── PageObjects/
│   ├── LoginPage.py
│   └── HomePage.py
│
├── TestCases/
│   ├── test_login.py
│   └── test_home.py
│
├── Utilities/
│   ├── Logger.py
│   ├── ReadProperties.py
│   └── XLUtils.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move to project

```bash
cd pytest-selenium-framework
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Test Cases

Run all tests

```bash
pytest
```

Run with HTML report

```bash
pytest --html=Reports/report.html --self-contained-html
```

Run specific test

```bash
pytest TestCases/test_login.py
```

Run in verbose mode

```bash
pytest -v
```

---

## Features

- Page Object Model (POM)
- Explicit Waits
- Config File Support
- Logging
- Screenshot on Failure
- HTML Reports
- Excel Data Driven Testing
- Cross Browser Support
- Reusable Utilities

---

## Reports

HTML reports are generated inside:

```
Reports/
```

---

## Screenshots

Failed test screenshots are saved in:

```
Screenshots/
```

---

## Configuration

Application URL, browser and other settings are managed from:

```
Configuration/config.ini
```

---

## Author

Automation Test Framework using Python + Selenium + Pytest.
