# Information to insert in our Database Tables
import sqlite3

# Data for Purpose
purpose_data = [
    (1, "There is an up-to-date board charter in place appropriate to the life-stage of the organisation and its current structure."),
    (2, "There is an up-to-date delegation of authority policy in place, which is effectively monitored."),
    (3, "The managing director's report effectively communicates status, identifies issues, and clearly indicates a linkage to the business plan."),
    (4, "Board packs are structured and used effectively to guide the board to make decisions and hold those authorised to make decisions accountable."),
    (5, "The board calendar is up-to-date and relevant for the timing requirements of the enterprise and its strategic focus."),
    (6, "All board meeting dates (and committee dates if applicable) for the year are scheduled indirectors' diaries and align with the board calendar."),
    (7, "The organisation has an up-to-date strategy (identifying the companies purpose and mediumterm vision) and a business plan (identifying the necessary next steps) that guides its focus and direction."),
    (8, "The board ensures a strategic focus in every board meeting to ensure that board papers relevant to the theme agreed upon for that meeting are prepared and that necessary key strategic issues are addressed proactively."),
    (9, "There is clarity regarding the organisation's culture, values, and beliefs"),
    (10, "The culture and values of the organisation are demonstrated by the board, setting the appropriate tone for the rest of the organisation to follow"),
    (11, "The board's conduct is characterised by trust, respect, candour, professionalism, accountability, diligence and commitment"),
    (12, "The organisation has developed a culture of accountability for performance."),
    (13, "The board committees (where appropriate) have approved terms of reference."),
    (14, "The board committees (where appropriate) have an agreed work plan for the year and are making good progress against that plan"),
]

# Data for Performance
performance_data = [
    (1, "The chairman and managing director meet before every board meeting, and this engagement delivers value to the board's focus and preparation, as well as enhancing the relationship between the board and management."),
    (2, "Independent directors meet before every board meeting and utilise this engagement to focus on value creation and enhance effective governance implementation."),
    (3, "The board is effective at passing resolutions based on thorough discussions and the information presented in board papers."),
    (4, "Shareholder-managers demonstrate their acceptance of the authority of the board."),
    (5, "There is a succession plan in place for the chief executive and this plan is proceeding as designed."),
    (6, "The chief executive/managing director has KPIs (Key Performance Indicators) in place and is held accountable for their performance against these indicators."),
    (7, "Board papers are distributed to the board at least seven working days prior to each board meeting."),
    (8, "An updated performance or measurement dashboard is provided in every set of board papers."),
    (9, "The measurement dashboard is used effectively and enables to board to predict the likely future performance of the organisation."),
    (10, "The chief executive/managing director's report is well-designed to be substantially comprehensive and provide an accurate reflection of the performance of the organisation. "),
    (11, "Every board meeting takes place."),
    (12, "Directors attend every scheduled board meeting"),
    (13, "All directors of the board are prompt at reviewing circulated minutes and providing feedback, ideally within two working days."),
    (14, "Directors are rotated every three years or as per the board charter"),
]

# Insert data into Sustainability Table
sustainability_data = [
        (1, "All relevant and strategic (material) internal and external stakeholders have been identified"),
        (2, "Stakeholder requirements (needs, interests, and expectations) are regularly assessed and understood to ensure the delivery of long-term, sustainable benefits."),
        (3, "There is a strategic approach to stakeholder engagement that ensures that the board and the rest of the organisation engage with stakeholders appropriately."),
        (4, "The organisation holds an annual general meeting every year"),
        (5, "The annual general meeting is effective at formally engaging shareholders"),
        (6, "The expectations of shareholders are understood, including both financial and non-financial outcomes, and the board manages these expectations so that they are more realistic where necessary."),
        (7, "The value that the organisation seeks is sustainable over time and meets the needs and expectations of shareholders, stakeholders and interested parties alike."),
        (8, "The audited annual financial statements are available for the previous year-end."),
        (9, "The board has determined the organisation's risk appetite and tolerance levels across all dimensions of the organisation's operations and performance."),
        (10, "A risk framework has been defined and implemented in line with this risk appetite and tolerance."),
        (11, "This risk framework facilitates the regular examination of both the internal operations of the organisation and the external environment to identify risks and implement mitigation strategies"),
        (12, "All risks are managed appropriately in line with the risk management framework"),
        (13, "The organisation acts in a socially responsible manner and delivers on its CSR (Community Social Responsibility) plan."),
        (14, "The organisation operates in an environmentally sustainable manner and reports on its environmental impact."),
]

# Insert data into Conformance Table
conformance_data = [
    (1, "Directors understand the contents of the organisation’s incorporation and founding documents (organisation constitution or memorandum of incorporation or other such documents)."),
    (2, "The appointed directors have been duly registered as directors of the organisation with the relevant companies' commission."),
    (3, "Each board director maintains an up-to-date conflict of interest register."),
    (4, "The organisation’s directors’ and officers’ liability insurance is current and sufficient."),
    (5, "There is a regular policy review process that enables the board to receives, review and approves both new and updated organisation policies on a regular basis."),
    (6, "The board, and each individual director, understand the financial model, activities and performance of the organisation"),
    (7, "The monthly financial measures that are tracked are up-to-date and actively monitored."),
    (8, "The financial report includes an income statement, balance sheet, cash flow forecast and financial ratios."),
    (9, "The monthly financial reports indicate that profitability, business value and solvency are improving."),
    (10, "The organisation has met solvency requirements."),
    (11, "The executive team has the necessary financial understanding and competence, supported by a finance manager, chief financial officer or outsourced provide who leads this element of the organisation's management."),
    (12, "An objective and regular operational assessment is actively used to monitor and evaluate organisation performance and focus ongoing improvement activity within the organisation."),
    (13, "An objective and regular governance assessment or evaluation is actively used by the board to monitor its own performance and cultivate a culture of continuous improvement of the board."),
    (14, "Directors regularly attend director training and continuous professional development, and demonstrate their commitment to continuous learning."),
]


def insertPurposeQuestions(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    cursor.executemany('INSERT INTO Purpose (purpose_id, purpose_question) VALUES (?, ?)', purpose_data)
    
    connect.commit()
    connect.close()
    
    
def insertPerformanceQuestions(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    cursor.executemany('INSERT INTO Performance (performance_id, performance_question) VALUES (?, ?)', performance_data)
    
    connect.commit()
    connect.close()
    
    
def insertSustainabilityQuestions(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    cursor.executemany('INSERT INTO Sustainability (sustainability_id, sustainability_question) VALUES (?, ?)', sustainability_data)
    
    connect.commit()
    connect.close()
    
    
def insertConformanceQuestions(database):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    cursor.executemany('INSERT INTO Conformance (conformance_id, conformance_question) VALUES (?, ?)', conformance_data)
    
    connect.commit()
    connect.close()


def allQuestionsGenerated(database):
    insertPurposeQuestions(database)
    insertSustainabilityQuestions(database)
    insertPerformanceQuestions(database)
    insertConformanceQuestions(database)
    
    print('Questions are now ready')
    

# Add All Responses from the user
def addResponses(database, data):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect(database)
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    directorID = getDirectorEmail()

    

    cursor.executemany('INSERT INTO Responses (response_id, directors_id, question_id, table_name ,response_value ) VALUES (?,?,?,?,?)', (2,directorID,3,'Sustainability', 2))
    connect.commit()
    connect.close()


def getDirectorEmail(email):
    # Connect to database or create it if file is not there
    connect = sqlite3.connect('company.db')
    # Execute SQL statements and fetch results from SQL queries
    cursor = connect.cursor()
    
    email = email['email']
    
    res = cursor.execute(f"SELECT director_id FROM CompanyName WHERE director_email == 'nick@gmail.com' " )
    
    return res.fetchone()

    
def getAnswers(answers):
    

# Connect to database or create it if file is not there
# connect = sqlite3.connect('company.db')
# # Execute SQL statements and fetch results from SQL queries
# cursor = connect.cursor()

# res = cursor.execute('SELECT * FROM CompanyName WHERE director_email == ' + email )

# connect.close()




