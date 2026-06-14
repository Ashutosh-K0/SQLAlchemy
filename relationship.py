from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Insert, Select, ForeignKey, Float, func

engine = create_engine('sqlite:///relationship_database.db', echo = True)

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

# A Python object representing the table.
things = Table(
    "things",
    meta,
    Column('id', Integer, primary_key=True),
    Column('description', String, nullable=False),
    Column('owner', Integer, ForeignKey('people.id')),
    Column('value', Float, nullable=False)
)

#Take all tables stored in Metadata and create them in the database.
meta.create_all(engine)

# Object that can be used to run commands and functions.
conn = engine.connect()

insert_people = people.insert().values([
    {'name': 'Ashu', 'age': 22},
    {'name': 'Mike', 'age': 21},
    {'name': 'Bob', 'age': 30},
    {'name': 'Clara', 'age':32},
    {'name': 'John', 'age': 42}
])

insert_things = things.insert().values([
    {'owner': 2, 'description': 'Laptop', 'value': 800.50},
    {'owner': 2, 'description': 'Mouse', 'value': 50.50},
    {'owner': 2, 'description': 'Keyboard', 'value': 100.50},
    {'owner': 3, 'description': 'Books', 'value': 30},
    {'owner': 4, 'description': 'Speakers', 'value': 80.50},
    {'owner': 5, 'description': 'Bottle', 'value': 10}
])

# conn.execute(insert_people)
# conn.commit()

# conn.execute(insert_things)
# conn.commit()

#Checking if the data was successfully inserted or not
select_statement = things.select()
result = conn.execute(select_statement)

select_statement_1 = people.select()
result_1 = conn.execute(select_statement)

join_statement = people.join(things, people.c.id == things.c.owner)
select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)

result = conn.execute(select_statement)

for row in result.fetchall():
     print(row)

group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(things.c.owner)
result = conn.execute(group_by_statement)

for row in result.fetchall():
    print(row)
