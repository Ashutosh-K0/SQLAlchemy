from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Insert, Select

engine = create_engine('sqlite:///core_database.db', echo = True)

#Creates a Metadata object. Think of MetaData as a container that stores information about tables.
meta = MetaData()

# A Python object representing the table.
people = Table(
    "people",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False)
)

#Take all tables stored in Metadata and create them in the database.
meta.create_all(engine)

# Object that can be used to run commands and functions.
conn = engine.connect()
insert_statement = Insert(people).values(name = 'Kumar', age = 20)
conn.execute(insert_statement)
conn.commit()

update_statement = people.update().where(people.c.name == "Kumar").values(name='Ash')
result = conn.execute(update_statement)

delete_statement = people.delete().where(people.c.id == 4)
conn.execute(delete_statement)
conn.commit()

select_statement = Select(people).where(people.c.name=='Ash')
result = conn.execute(select_statement)

for row in result.fetchall():
    print(row)