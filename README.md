# CLI Contact Manager

A Python-based Command Line Contact Manager that allows users to manage personal contact information directly through the terminal.

The application provides a simple way to store and access contact details, including names and phone numbers. It uses JSON for data storage, ensuring that saved contacts remain available even after the application is closed.

## Features

- **Add Contact:** Add a new contact by entering their name and phone number.
- **View Contacts:** Display all saved contacts in a numbered list.
- **Persistent Storage:** Automatically save contact information in a JSON file.
- **Data Retrieval:** Load previously saved contacts whenever the application starts.
- **Modular Architecture:** Separate contact management operations from data storage logic.

## Tech Stack

- Python 3
- JSON
- Python Standard Library

## Project Structure

```text
contact-manager/
│
├── main.py
├── contacts.py
├── storage.py
├── contacts.json
├── .venv/
└── README.md
```

## Application Architecture

The application is organized into three main Python modules:

**main.py**
- Entry point of the application.
- Controls the application flow and user interaction.

**contacts.py**
- Handles contact-related operations.
- Contains functions for adding and displaying contacts.

**storage.py**
- Manages JSON-based data storage.
- Loads existing contacts and saves updated contact records.

**contacts.json**
- Stores contact information in a structured JSON format.

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project

```bash
cd contact-manager
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 5. Run the application

```bash
python main.py
```

## Data Storage

Contact records are stored locally in `contacts.json`.

Each contact follows this structure:

```json
{
    "name": "John",
    "phone": "9876543210"
}
```

The application reads from and writes to this file to maintain contact records
