# gadgetkart
Gadget Kart - Mobile Selling website

# Flask GadgetKart Site with MySQL

This project demonstrates a simple web application using Flask for the backend, a MySQL database to store contact form submissions, and HTML templates for the frontend.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

Install dependencies:

pip install Flask Flask-MySQL
Configuration
Edit the app.py file to configure your MySQL database:

python
# Configure MySQL
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_mysql_database'

Usage
Run the Flask application:
python app.py
Visit http://127.0.0.1:5000/ in your browser to access the application.

Directory Structure
app.py: Main Flask application file.
templates/: HTML templates used by Flask.

