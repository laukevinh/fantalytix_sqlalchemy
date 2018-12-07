from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, Integer, String, Date,
    DateTime)

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    __table_args__ = {'schema':'fantalytix'}

    # Add sequence

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    height = Column(String(7))
    weight = Column(Integer)
    birthday = Column(Date)
    birthplace = Column(String(100))
    nationality = Column(String(50))
    created_by = Column(String(255))
    creation_date = Column(DateTime)
    last_updated_by = Column(String(255))
    last_updated_date = Column(DateTime)

    def __repr__(self):
        return "<Player(name='{name}')>".format(name = self.name)
