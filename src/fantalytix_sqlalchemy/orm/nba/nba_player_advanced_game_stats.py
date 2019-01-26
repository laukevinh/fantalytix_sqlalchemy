from sqlalchemy import (
    Column, BigInteger, Integer, Time, Float, SmallInteger, PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship, remote, foreign

from ..common.base import Base
from ..common.audit_entity import AuditEntity

class NBAPlayerAdvancedGameStats(Base, AuditEntity):
    __tablename__ = 'nba_player_advanced_game_stats'
    __table_args__ = (
        PrimaryKeyConstraint(
            'nba_game_id', 
            'player_id', 
            name='nba_player_advanced_game_stats_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    nba_game_id = Column(BigInteger, nullable=False)
    player_id = Column(BigInteger, nullable=False)
    team_id = Column(Integer, nullable=False)
    minutes_played = Column(Time)
    true_shooting_percentage = Column(Float)
    effective_field_goal_percentage = Column(Float)
    three_point_attempt_rate = Column(Float)
    free_throw_attempt_rate = Column(Float)
    offensive_rebound_percentage = Column(Float)
    defensive_rebound_percentage = Column(Float)
    total_rebound_percentage = Column(Float)
    assist_percentage = Column(Float)
    steal_percentage = Column(Float)
    block_percentage = Column(Float)
    turnover_percentage = Column(Float)
    usage_percentage = Column(Float)
    offensive_rating = Column(SmallInteger)
    defensive_rating = Column(SmallInteger)
    nba_game = relationship("NBAGame",
        primaryjoin=("remote(NBAGame.id)=="
                     "foreign(NBAPlayerAdvancedGameStats.nba_game_id)")
    )
    player = relationship("Player",
        primaryjoin=("remote(Player.id)=="
                     "foreign(NBAPlayerAdvancedGameStats.player_id)")
    )
    team = relationship("Team",
        primaryjoin=("remote(Team.id)=="
                     "foreign(NBAPlayerAdvancedGameStats.team_id)")
    )

    def __repr__(self):
        return (
            "<NBAPlayerAdvancedGameStats("
                "player='{}', "
                "team='{}', "
                "game_date='{}'"
            ")>".format(
                self.player.name,
                self.team.abbreviation,
                self.nba_game.get_game_date()
            )
        )
