from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, Integer, String, DateTime)

from orm.common.audit_entity import AuditEntity

Base = declarative_base()

class League(Base, AuditEntity):
    __tablename__ = 'leagues'
    __table_args__ = {'schema':'fantalytix'}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    abbreviation = Column(String(25))
    sport = Column(String(50), nullable=False)

    def __repr__(self):
        return "<League(abbreviation='{}')>".format(self.abbreviation)
