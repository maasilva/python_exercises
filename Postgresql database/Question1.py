import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "yourpassword",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "python_db")

    cursor = connection.cursor()
    
    create_table_query = '''CREATE TABLE IF NOT EXISTS Hospital
          (Hospital_Id serial NOT NULL PRIMARY KEY, 
	Hospital_Name VARCHAR (100) NOT NULL, 
	Bed_Count serial); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    
    create_table_query = '''CREATE TABLE IF NOT EXISTS Doctor ( 
	Doctor_Id serial NOT NULL PRIMARY KEY, 
	Doctor_Name VARCHAR (100) NOT NULL, 
	Hospital_Id serial NOT NULL, 
	Joining_Date DATE NOT NULL, 
	Speciality VARCHAR (100) NOT NULL, 
	Salary INTEGER NOT NULL,
	Experience SMALLINT);'''
    
    cursor.execute(create_table_query)
    connection.commit()

    postgres_insert_query = """ INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) VALUES (%s,%s,%s)"""
    record_to_insert =('1', 'Mayo Clinic', 200)
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()

    postgres_insert_query = """ INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) VALUES (%s,%s,%s)"""
    record_to_insert =('2', 'Cleveland Clinic', 400)
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()

    postgres_insert_query = """ INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) VALUES (%s,%s,%s)"""
    record_to_insert =('3', 'Johns Hopkins', 1000)
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()

    postgres_insert_query = """ INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) VALUES (%s,%s,%s)"""
    record_to_insert =('4', 'UCLA Medical Center', 1500)
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()

    postgres_insert_query = """ INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert =('101', 'David', '1', '2005-2-10', 'Pediatric', '40000')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    
    postgres_insert_query = """ INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert =('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    
    postgres_insert_query = """ INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert =('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    
    postgres_insert_query = """ INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert =('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    
    postgres_insert_query = """ INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert =('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    
    postgres_insert_query = """ INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert =('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    
    postgres_insert_query = """ INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert =('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    
    postgres_insert_query = """ INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert =('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()

    count = cursor.rowcount

    print(count, "Table created and inserts successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
