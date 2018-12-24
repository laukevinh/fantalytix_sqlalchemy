from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, Integer, 
    String, Date, PrimaryKeyConstraint)

from fantalytix_sqlalchemy.orm.common.audit_entity import AuditEntity

Base = declarative_base()

class DraftPick(Base, AuditEntity):
    __tablename__ = 'draft_picks'
    __table_args__ = (
        PrimaryKeyConstraint(
            'season_id',
            'overall_pick', 
            name='draft_picks_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    season_id = Column(Integer, nullable=False)
    round = Column(Integer, nullable=False)
    pick_in_round = Column(Integer, nullable=False)
    overall_pick = Column(Integer, nullable=False)
    team_id = Column(Integer, nullable=False)
    player_id = Column(BigInteger, nullable=False)

    def __repr__(self):
        return "<DraftPick(season_id={}, overall_pick='{}')>".format(
            self.season_id, self.overall_pick)
