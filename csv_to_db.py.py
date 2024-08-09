import csv

# Path to your CSV file
csv_file_path = 'games_dataset.csv'

# List to hold the dictionaries
data_list = []

# Open and read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Add each row as a dictionary to the list
        data_list.append(row)

# Print the list of dictionaries
for item in data_list:
    print(item)
import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('games.db')  # Replace with your database file path
cursor = conn.cursor()

# Define the table creation SQL (if needed)
create_table_sql = '''
CREATE TABLE IF NOT EXISTS games (
    "Game Name" TEXT,
    "Genre" TEXT,
    "Platform" TEXT,
    "Release Year" INTEGER,
    "User Rating" REAL
);
'''
cursor.execute(create_table_sql)

# Define the SQL insert statement
insert_sql = '''
INSERT INTO games ("Game Name", "Genre", "Platform", "Release Year", "User Rating")
VALUES (?, ?, ?, ?, ?);
'''

# Insert the data into the database
for data in data_list:
    values = (
        data['Game Name'],
        data['Genre'],
        data['Platform'],
        int(data['Release Year']),
        float(data['User Rating'])
    )
    cursor.execute(insert_sql, values)

# Commit the transaction and close the connection
conn.commit()
conn.close()
