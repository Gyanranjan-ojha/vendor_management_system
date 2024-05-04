# Vendor Management System

## Overview
This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Prerequisites

Before installing the DQH Admin Tool, ensure you have the following installed:

- Python (version 3.10 or higher)
- Git (version 2.42 or higher)


## Installation

**1. Clone the project**

```bash
  git clone https://github.com/Gyanranjan-ojha/vendor_management_system.git
```

**2. Navigate to the vendor_management_system directory**

```bash
  cd vendor_management_system
```

**3. Pull from 'main' branch**

```bash
  git pull origin main
```

## Project Setup

- Create a virtual environment

```bash
  python -m venv venv
```

- Activate the virtual environment

- For Ubuntu

```bash
  source venv/bin/activate
```

- For Windows

```bash
  venv/Scripts/activate
```

- Install python dependencies

```bash
  pip install -r requirements.txt
```

- .env Configuration

Create a `.env` file in the vendor_management_system directory and provide the necessary environment variables:

```bash
  export AUTH_TOKEN='<AUTH_TOKEN>' # mix of alphabet,numbers,special characters with more than 20 letters.
```

- Migrate the Database for creating tables by django commands

```bash
  python manage.py makemigrations app
  python manage.py migrate
```

- Starting the Django Server

```bash
  python manage.py runserver
```

## Tech Stack

**Server:** Django REST Framework

**Database:** Sqlite Database