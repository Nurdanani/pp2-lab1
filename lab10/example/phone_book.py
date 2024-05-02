import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='phone_book', 
    user='postgres', 
    password='nurdana2006',
    port='2903'
    )
# Create a cursor to work with the database
cur = conn.cursor()

# Delete table
cur.execute('DROP TABLE phone_book;')

conn.commit()

# Create a new table
cur.execute("""CREATE TABLE phone_book (
            name VARCHAR(255),
            phone_number VARCHAR(20)
);
""")

conn.commit()

cur.execute("""INSERT INTO phone_book (name, phone_number) VALUES
            ('Asylym', '+7759560235'),
            ('Nazar', '+7078430295'),
            ('Tomiris', '+7783597014');
            """)

conn.commit()

#Get people
cur.execute('SELECT name FROM phone_book')

print(cur.fetchall())

cur.execute('SELECT name FROM phone_book')

print(cur.fetchone())

conn.commit()

cur.execute("""UPDATE phone_book
            SET phone_number = '+7026363365' 
            WHERE name='Tomiris';""")

conn.commit()

#delete person
cur.execute("""DELETE FROM phone_book
            WHERE name = 'Nazar';""")

conn.commit()