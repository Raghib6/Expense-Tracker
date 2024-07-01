# ExpenseTracker

ExpenseTracker is a Django-based web application designed to help users track their expenses, set budgets, filter expenses by various criteria, and receive alerts when budgets are exceeded. This project aims to provide a comprehensive and user-friendly platform for personal financial management.

## Features

- **Expense Logging:** Record daily expenses with details like amount, category, and description.
- **Budget Setting:** Set budgets for different categories.
- **Filtering Expenses:** Filter expenses by date range, category.
- **Summary Reports:** View summary reports of your expenses to get insights into your spending habits.
- **Budget Alerts:** Receive alerts when your spending exceeds the set budget for any category.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- Django 3.x or later
- SQLite (default database)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/raghib6/ExpenseTracker.git
   cd ExpenseTracker
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv ve
   source ve/bin/activate  # On Windows use `ve\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000/homepage/` to access the application.

## Usage

1. **Log In:**
   - Log in with the superuser account created during installation.
2. **Add Expenses:**
   - Navigate to the "Add Expense" section to log your expenses.
3. **Set Budgets:**
   - Go to the "Set Budget" section to set your budgets.
4. **Add Expense:**
   - Go to the "Add Expense" section to add your expenses.
5. **View Budget Summary:**
   - Go to the "Budget Summary" section to view budget summary reports of your expenses.
6. **Receive Alerts:**
   - Simple Alert on Home Page

## Project Structure

```
ExpenseTracker/                 # Root directory of the project
├── ExpenseTracker/             # Main Django project folder
├── templates/                  # Directory for HTML templates
├── tracker_app/                # Main application directory for tracking expenses
├── ve/                         # Virtual environment directory
├── db.sqlite3                  # SQLite database file
├── manage.py                   # Django management script
├── README.md                   # Project README file
├── requirements.txt            # List of project dependencies

```
