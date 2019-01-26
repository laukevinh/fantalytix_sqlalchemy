from sqlalchemy import (
    Column, BigInteger, Integer, Boolean, Time, SmallInteger, Float, 
    PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship, remote, foreign

from ..common.base import Base
from ..common.audit_entity import AuditEntity

class NBAPlayerBasicGameStats(Base, AuditEntity):
    __tablename__ = 'nba_player_basic_game_stats'
    __table_args__ = (
        PrimaryKeyConstraint(
            'nba_game_id', 
            'player_id', 
            name='nba_player_basic_game_stats_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    nba_game_id = Column(BigInteger, nullable=False)
    player_id = Column(BigInteger, nullable=False)
    team_id = Column(Integer, nullable=False)
    is_starter = Column(Boolean)
    minutes_played = Column(Time)
    field_goals_made = Column(SmallInteger)
    field_goals_attempted = Column(SmallInteger)
    field_goal_percentage = Column(Float)
    three_pointers_made = Column(SmallInteger)
    three_pointers_attempted = Column(SmallInteger)
    three_point_percentage = Column(Float)
    free_throws_made = Column(SmallInteger)
    free_throws_attempted = Column(SmallInteger)
    free_throw_percentage = Column(Float)
    offensive_rebounds = Column(SmallInteger)
    defensive_rebounds = Column(SmallInteger)
    total_rebounds = Column(SmallInteger)
    assists = Column(SmallInteger)
    steals = Column(SmallInteger)
    blocks = Column(SmallInteger)
    turnovers = Column(SmallInteger)
    personal_fouls = Column(SmallInteger)
    points = Column(SmallInteger)
    plus_minus = Column(SmallInteger)
    nba_game = relationship("NBAGame",
        primaryjoin=("remote(NBAGame.id)=="
                     "foreign(NBAPlayerBasicGameStats.nba_game_id)")
    )
    player = relationship("Player",
        primaryjoin=("remote(Player.id)=="
                     "foreign(NBAPlayerBasicGameStats.player_id)")
    )
    team = relationship("Team",
        primaryjoin=("remote(Team.id)=="
                     "foreign(NBAPlayerBasicGameStats.team_id)")
    )

    def __repr__(self):
        return (
            "<NBAPlayerBasicGameStats("
                "player='{}', "
                "team='{}', "
                "game_date='{}'"
            ")>".format(
                self.player.name,
                self.team.abbreviation,
                self.nba_game.get_game_date()
            )
        )
