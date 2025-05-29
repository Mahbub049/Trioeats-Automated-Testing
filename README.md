# 🍽️ TrioEats Automated Testing with Selenium

This project contains automated test scripts for the [TrioEats](https://trioeats-8ebfe.web.app) web application using **Selenium WebDriver with Python**. The tests cover critical flows such as login, registration, profile update, and logout to ensure consistent functionality across user interactions.

---

## 📁 Project Structure

```
trioeats-qa-selenium/
│
├── drivers/                  # Contains ChromeDriver
├── reports/                  # HTML reports generated after tests
├── tests/                    # Selenium test scripts
│   ├── test_login.py
│   ├── test_register.py
│   ├── test_invalid_login.py
│   ├── test_invalid_register.py
│   ├── test_logout.py
│   └── test_profile_update.py
│
├── requirements.txt          # List of required packages
└── README.md                 # Project documentation
```

---

## 🔍 Features Covered

| Feature                        | Test File                   | Status    |
|-------------------------------|-----------------------------|-----------|
| ✅ Valid Login                | `test_login.py`             | Completed |
| ❌ Invalid Login              | `test_invalid_login.py`     | Completed |
| ✅ Valid Registration         | `test_register.py`          | Completed |
| ❌ Invalid Registration       | `test_invalid_register.py`  | Completed |
| 🔒 Logout Functionality       | `test_logout.py`            | Completed |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/trioeats-qa-selenium.git
cd trioeats-qa-selenium
```

### 2. Install Dependencies

Make sure Python and pip are installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Add ChromeDriver

Download and place `chromedriver.exe` (matching your Chrome version) inside the `drivers/` folder.

---

## ▶️ Running the Tests

### Run All Tests with HTML Report

```bash
pytest tests/ --html=reports/full_report.html
```

### Run a Specific Test

```bash
pytest tests/test_login.py --html=reports/login_report.html
```

> Reports are generated in the `reports/` folder and viewable in any browser.

---

## 📌 Notes

- Framework: **Selenium WebDriver**
- Language: **Python 3**
- Test Runner: **pytest**
- Reporting: **pytest-html**
- Browser: **Google Chrome**

---

## 🤝 Contribution Guidelines

If you'd like to contribute:
1. Fork this repo
2. Create a branch: `git checkout -b feature/test-case`
3. Commit your changes: `git commit -m "Add test case"`
4. Push to the branch: `git push origin feature/test-case`
5. Open a Pull Request

---

## 👤 Author

**Muhammad Mahbub Sarwar**  
Lecturer & QA Automation Enthusiast  
🔗 [LinkedIn Profile](https://linkedin.com)

---

## 📃 License

This project is licensed under the MIT License. See `LICENSE` for details.
