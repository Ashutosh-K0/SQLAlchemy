from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

#It creates an Engine object, which acts as SQLAlchemy's interface to our database. Responsible for the database connection, managing connection pool, sending SQL queries to the database, recieving results from the database. Database URL is passed here as value.
engine = create_engine("sqlite:///mydatabase.db", echo = True)

#"conn" object is the connection object that now can be used to run commands
conn = engine.connect()

# To Create Table
conn.execute(text("CREATE TABLE IF NOT EXISTS people(name str, age int)"))
conn.commit()

#A Session in SQLAlchemy is a high-level database interaction object that manages transactions, tracks changes to ORM objects, executes queries, and communicates with the database through the Engine. In ORM-based applications, the Session is the primary interface used to read and write data.
session = Session(engine)
session.execute(text('INSERT INTO people VALUES("Ashutosh", 22);'))
session.commit()

result = session.execute(text('SELECT * FROM people;'))
session.commit()

for row in result:
    print(row)