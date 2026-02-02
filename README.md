# Leave Request System

A simple Django application for managing employee leave requests.

## Features

- **List Leave Requests**: View all submitted leave requests with calculated leave days (excluding weekends).
- **Submit Request**: Create new leave requests for staff.
- **Edit Request**: Update existing leave request details.
- **Weekend Exclusion**: Automatically calculates the number of working days for a leave period.

## Logic Overview

The core logic for calculating leave days is located in the `LeaveRequest` model. It iterates through the dates between the start and end date and counts only weekdays (Monday-Friday).

## Installation

1.  **Clone or download the repository.**
2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Apply database migrations:**

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

2.  **Start the development server:**

    ```bash
    python3 manage.py runserver
    ```

3.  **Access the application:**
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Running Tests

To run the automated tests:

```bash
python3 manage.py test
```
