import sqlite3
from insertDB import allQuestionsGenerated

# Create Employees table
# For Login
def createSirdar(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            employee_id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            
        );
    ''')
    
    connect.commit()
    connect.close()


# Create Purpose Table
def createPurposeTable(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Purpose (
            purpose_id INTEGER PRIMARY KEY,
            purpose_question TEXT
        )
    ''')
    
    print('Purpose Table successfully created')


    connect.commit()
    connect.close()


# Create Performance Table
def createPerformanceTable(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Performance (
            performance_id INTEGER PRIMARY KEY,
            performance_question TEXT
        )
    ''')
    
    print('Performance Table successfully created')

    connect.commit()
    connect.close()


# Create Sustainability Table
def createSustainabilityTable(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sustainability (
            sustainability_id INTEGER PRIMARY KEY,
            sustainability_question TEXT
        )
    ''')
    
    print('Sustainability Table successfully created')

    connect.commit()
    connect.close()


# Create Conformance Table
def createConformanceTable(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Conformance (
            conformance_id INTEGER PRIMARY KEY,
            conformance_question TEXT
        )
    ''')
    
    print('Conformance Table successfully created')

    
    connect.commit()
    connect.close()


# Create CompanyName Table
def createCompanyNameTable(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CompanyName (
            director_id INTEGER PRIMARY KEY,
            director_email TEXT
        )
    ''')

    print('CompanyName Table successfully created')

    connect.commit()
    connect.close()


# Create Responses Table
def createResponsesTable(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Responses (
        response_id SERIAL PRIMARY KEY,
        directors_id INT,
        question_id INT,
        table_name VARCHAR(50), -- To store the name of the table (Purpose, Sustainability, etc.)
        response_value INT CHECK (response_value BETWEEN 0 AND 4),
        
        FOREIGN KEY (directors_id) REFERENCES CompanyName(directors_id)
    )
    ''')
    
    print('Responses Table successfully created')

    connect.commit()
    connect.close()


# Create all the tables for a database
def addAllTables(database):
    createCompanyNameTable(database)
    createPurposeTable(database)
    createPerformanceTable(database)
    createConformanceTable(database)
    createSustainabilityTable(database)
    createResponsesTable(database)
    allQuestionsGenerated(database)
    
    
addAllTables('company.db')

