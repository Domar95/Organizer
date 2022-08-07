import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('db_username')
PASSWORD = os.getenv('db_password')

db = mysql.connector.connect(
    host='localhost', user=USERNAME, password=PASSWORD, database='testrecorddb')

mycursor = db.cursor()

# mycursor.execute(
#    'CREATE TABLE DailyGoal (dailyGoalID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), text VARCHAR(100), generalCategory VARCHAR(50), importance smallint UNSIGNED, date VARCHAR(20), duration smallint UNSIGNED)')

# print(mycursor)
#mycursor.execute('DESCRIBE DailyGoal')

# for x in mycursor:
#    print(x)

# print(mycursor)

# mycursor.execute("INSERT INTO DailyGoal (name, text, generalCategory, importance, date, duration) VALUES (%s,%s,%s,%s,%s,%s)",
#                 ('workout', '3 times a week gym workout', 'object (reference general-cat obj)/another table', 8, '07.08.2022', 90))

# db.commit()


#mycursor.execute("SELECT * FROM DailyGoal")

# for x in mycursor:
#    print(x)
