from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, Integer, String, Date,
    DateTime)

from fantalytix_sqlalchemy.orm.common.audit_entity import AuditEntity

Base = declarative_base()

class Player(Base, AuditEntity):
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

    def __repr__(self):
        return "<Player(name='{name}')>".format(name = self.name)
