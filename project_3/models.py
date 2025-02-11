from sqlalchemy import Boolean, Column, Integer, String
from database import Base   

# In this code we have created a table called todos and we have added all the necessary Information to it with its default values and datatypes.
class Todos(Base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)