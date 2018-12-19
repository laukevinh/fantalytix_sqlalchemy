from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, Integer, 
    String, DateTime)

from orm.common.audit_entity import AuditEntity

Base = declarative_base()

class NBAGame(Base, AuditEntity):
    __tablename__ = 'nba_games'
    __table_args__ = {'schema':'fantalytix'}

    id = Column(BigInteger, primary_key=True, nullable=False)
    season_id = Column(Integer, nullable=False)
    home_team_id = Column(Integer, nullable=False)
    away_team_id = Column(Integer, nullable=False)
    game_date = Column(DateTime)
    home_score = Column(Integer, nullable=False)
    away_score = Column(Integer, nullable=False)
    overtimes = Column(Integer, nullable=False)
    winning_team_id = Column(Integer)
    status = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)

    def __repr__(self):
        return "<NBAGame(home_team_id={}, date='{}')>".format(
            self.home_team_id, self.game_date.strftime('%Y/%m/%d'))
