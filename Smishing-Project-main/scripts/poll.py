import mysql.connector
import os

# Connect to the database
host = "72.167.87.111"
user = "users"
password = "CECS378group8"
database = "userinput"
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Get the latest row ID that we processed
last_id_processed_str = open('last_id_processed.txt', 'r').read().strip()
last_id_processed = int(last_id_processed_str) if last_id_processed_str else 0


# Query the database for new rows since the last processed ID
cursor = conn.cursor(dictionary=True)
sql = "SELECT * FROM inputs WHERE id > %s"
cursor.execute(sql, (last_id_processed,))
rows = cursor.fetchall()

# Loop through the new rows and create the .csv files
for row in rows:
    filename = os.path.join(os.path.dirname(__file__), str(row['id']) + ".csv")
    output = "Input 1,Input 2\n" + row['input1'] + "," + row['input2']
    with open(filename, 'w') as f:
        f.write(output)

# Update the last processed ID
if rows:
    latest_id = rows[-1]['id']
else:
    latest_id = last_id_processed
with open('last_id_processed.txt', 'w') as f:
    f.write(str(latest_id))

cursor.close()
conn.close()
