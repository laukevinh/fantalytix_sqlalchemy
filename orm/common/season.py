from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, Integer, String, Date)

from orm.common.audit_entity import AuditEntity

Base = declarative_base()

class Season(Base, AuditEntity):
    __tablename__ = 'seasons'
    __table_args__ = {'schema':'fantalytix'}

    id = Column(Integer, primary_key=True, nullable=False)
    league_id = Column(Integer, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    start_year = Column(Date, nullable=False)
    end_year = Column(Date, nullable=False)

    def __repr__(self):
        return "<Season(league_id='{}', years='{}-{}')>".format(
            self.league_id, self.start_year.strftime("%Y"), 
            self.end_year.strftime("%y"))


