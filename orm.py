from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()

#Creating Tables using Classes
class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    things = relationship('Thing', back_populates='person')

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    owner_id = Column(Integer, ForeignKey('people.id'))

    person = relationship('Person', back_populates='things')

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

new_person = Person(name = 'Charlie', age = 70)
session.add(new_person)
session.flush()

new_thing = Thing(description = 'Camera', value = 50, owner_id = new_person.id)
session.add(new_thing)

session.commit()

print([t.description for t in new_person.things])
print(new_thing.person.name)