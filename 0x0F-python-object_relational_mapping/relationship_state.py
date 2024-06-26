#!/usr/bin/python3
"""state class defination and instance
Base = declarative_base() """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ State Class inherit from Base declarative_base()
    links to the MySQL table state
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='delete', backref="state")
