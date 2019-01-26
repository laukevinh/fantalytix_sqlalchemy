from sqlalchemy import (
    Column, BigInteger, Integer, String, DateTime, UniqueConstraint
)
from sqlalchemy.orm import relationship, remote, foreign

from ..common.base import Base
from ..common.audit_entity import AuditEntity

class NBAGame(Base, AuditEntity):
    __tablename__ = 'nba_games'
    __table_args__ = (
        UniqueConstraint(
            'game_date',
            'home_team_id',
            'away_team_id'),
        {
            'schema':'fantalytix',
        }
    )

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
    season = relationship("Season",
        primaryjoin="remote(Season.id)==foreign(NBAGame.season_id)"
    )
    home_team = relationship("Team",
        primaryjoin="remote(Team.id)==foreign(NBAGame.home_team_id)"
    )
    away_team = relationship("Team",
        primaryjoin="remote(Team.id)==foreign(NBAGame.away_team_id)"
    )
    winning_team = relationship("Team",
        primaryjoin="remote(Team.id)==foreign(NBAGame.winning_team_id)"
    )

    def get_game_date(self):
        return self.game_date.strftime('%Y/%m/%d')

    def __repr__(self):
        return "<NBAGame(home_team='{}', date='{}')>".format(
            self.home_team.abbreviation, self.get_game_date())
