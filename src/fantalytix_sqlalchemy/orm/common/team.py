from sqlalchemy import (Column, Integer, String, DateTime)

from .base import Base
from .audit_entity import AuditEntity

class Team(Base, AuditEntity):
    __tablename__ = 'teams'
    __table_args__ = {'schema':'fantalytix'}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False, unique=True)
    abbreviation = Column(String(10), nullable=False)
    status = Column(String(25), nullable=False)

    def __repr__(self):
        return "<Team(name='{}')>".format(self.name)
