from sqlalchemy import (Column, Integer, String, Date, UniqueConstraint)
from sqlalchemy.orm import relationship, remote, foreign

from .base import Base
from .audit_entity import AuditEntity

class Season(Base, AuditEntity):
    __tablename__ = 'seasons'
    __table_args__ = (
        UniqueConstraint(
            'league_id',
            'start_year',
            'end_year'),
        {
            'schema':'fantalytix',
        }
    )

    id = Column(Integer, primary_key=True, nullable=False)
    league_id = Column(Integer, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    start_year = Column(Date, nullable=False)
    end_year = Column(Date, nullable=False)
    league = relationship("League",
        primaryjoin="remote(League.id)==foreign(Season.league_id)"
    )

    def pretty_print_years(self):
        return '{}-{}'.format(
            self.start_year.strftime("%Y"), 
            self.end_year.strftime("%y")
        )

    def __repr__(self):
        return "<Season(league='{}', years='{}')>".format(
            self.league.abbreviation, self.pretty_print_years()
        )
