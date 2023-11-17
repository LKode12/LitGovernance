import sqlite3

# Connect to database or create it if file is not there
connect = sqlite3.connect('company.db')

# Execute SQL statements and fetch results from SQL queries
cursor = connect.cursor()

# Create Purpose Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Purpose (
        purpose_id INTEGER PRIMARY KEY,
        purpose_question TEXT
    )
''')

# Create Performance Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Performance (
        performance_id INTEGER PRIMARY KEY,
        performance_question TEXT
    )
''')


# Create Sustainability Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sustainability (
        sustainability_id INTEGER PRIMARY KEY,
        sustainability_question TEXT
    )
''')


# Create Conformance Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Conformance (
        conformance_id INTEGER PRIMARY KEY,
        conformance_question TEXT
    )
''')
