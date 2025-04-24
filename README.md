# ParaBank Selenium Automation Framework

A robust, scalable, and modular test automation framework for testing core banking functionalities on [ParaBank](https://parabank.parasoft.com/parabank/index.htm) using Python, PyTest, Selenium WebDriver, and enhanced reporting and logging.

---

## 🔍 Overview
This project automates several customer and admin functionalities in the ParaBank web application. It covers login, account creation, fund transfers, transaction history, and administrative backend control.

---

## ✅ Test Cases Implemented

### 1. TC_CUST_01_OpenNewAccount
**Objective**: Verify that a customer can open a new account successfully.

**Steps:**
1. Login using valid credentials.
2. Navigate to **Open New Account**.
3. Select Account Type: `SAVINGS` or `CHECKING`.
4. Choose an existing account to transfer initial deposit.
5. Click on **Open New Account**.
6. Capture and verify the account number and success message.

**Assertions:**
- The new account number is displayed.
- Message: `"Your new account has been successfully created."`

---

### 2. TC_CUST_03_TransferFunds
**Objective**: Ensure fund transfer between accounts is successful.

**Steps:**
1. Login to the ParaBank account.
2. Navigate to **Transfer Funds**.
3. Enter a valid transfer amount (e.g., 500).
4. Select "From Account" and "To Account".
5. Click on **Transfer**.
6. Confirm the success message.

**Assertions:**
- Message like `"Transfer Complete!"` is shown.
- Account balances are adjusted (manual or UI verification).

---

### 3. TC_CUST_04_ViewTransactionHistory
**Objective**: Validate transaction history is correctly listed.

**Steps:**
1. Login to your customer account.
2. Click **Accounts Overview**.
3. Choose an account from the list.
4. Go to **Account Activity** / Transaction page.
5. Check if recent transactions are listed.

**Assertions:**
- Each row in the transaction table includes:
  - **Date**
  - **Description**
  - **Amount**

---

### 4. TC_ADMIN_01_AdminPageControls
**Objective**: Validate all functionalities on the Admin Page.

**Steps:**
1. Navigate to the **Admin Page**: `/admin.htm`
2. Click **Initialize** to reset database state.
3. Toggle **SOAP Service** to change the web service.
4. Choose **REST XML** or **REST JSON** mode for service API type.
5. Select appropriate data access mode (e.g., JDBC).
6. Click **Submit**.
7. Capture logs for confirmation.

**Assertions:**
- No errors/exceptions during the actions.
- The changes reflect correctly on the backend (UI/log confirmation).
- Log file shows:
  - Action confirmations
  - Successful execution

---

## 📁 Project Structure

```
ParaBank-Automation/
├── pageObjects/             # POM for page classes
├── testCases/               # PyTest test classes
├── utilities/               # Custom Logger, Config reader
├── reports/                 # HTML or Allure Reports
├── Screenshots/             # Failures capture
├── conftest.py              # Pytest fixtures
├── requirements.txt         # All dependencies
└── README.md
```

---

## 🧪 How to Run Tests

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Execute All Tests with HTML Report**
```bash
pytest -v --html=reports/report.html --self-contained-html
```

3. **Run Specific Test Case**
```bash
pytest testCases/test_open_account.py
```

---

## 📊 Reports & Logging
- **HTML Reports**: Via `pytest-html` plugin
- **Custom Logs**: Available in `/Logs/` directory per test case
- **Screenshots**: Captured for every failure in `/Screenshots/`

---

## ⚙️ Integrations (Optional Advanced Setup)

- **Allure Reports**
- **GitHub Actions** – Run tests on each push
- **Jenkins** – CI/CD integration
- **Docker** – Containerize entire framework


Happy Testing! 🚀

