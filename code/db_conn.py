import pypyodbc  

#creating SQL Server Connection  
conn = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server}};'
						'Server=REPLACE_WITH_YOUR_SERVER;'
						'Database=testdb;'
						'uid=REPLACE_ME_WITH_YOUR_USER;'
						'pwd=REPLACE_ME_WITH_YOUR_PASSWORD';)  

cursor = conn.cursor()   
  
#Executing the query  
cursor = conn.cursor()
cursor.execute('SELECT * FROM customers')

for i in cursor:
    print(i)
  
#closing connection  
conn.close()  
