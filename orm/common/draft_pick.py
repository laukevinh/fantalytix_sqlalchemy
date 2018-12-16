from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, Integer, 
    String, Date, PrimaryKeyConstraint)

from orm.common.audit_entity import AuditEntity

Base = declarative_base()

class DraftPick(Base, AuditEntity):
    __tablename__ = 'draft_picks'
    __table_args__ = (
        PrimaryKeyConstraint(
            'year', 
            'round', 
            'pick', 
            name='draft_picks_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    year = Column(Date, nullable=False)
    round = Column(Integer, nullable=False)
    pick = Column(Integer, nullable=False)
    team_id = Column(Integer, nullable=False)
    player_id = Column(BigInteger, nullable=False)
    league = Column(String(10), nullable=False)

    def __repr__(self):
        return "<DraftPick(year={}, pick='{}')>".format(
            self.year.strftime('%Y'), self.pick)
