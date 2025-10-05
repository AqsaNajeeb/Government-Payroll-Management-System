import oracledb

# Replace with your actual database credentials
username = "system"
password = "Khan@857052"
dsn = "localhost/orcl"  # Example: 127.0.0.1/orcl or your TNS service name

try:
    # Connect to the database in THIN mode (no need for Instant Client)
    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    print("✅ Connection successful!")

    # Create a cursor and fetch data
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM DEPARTMENT_T") 
    for row in cursor:
        print(row)

except oracledb.Error as error:
    print("❌ Error:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
