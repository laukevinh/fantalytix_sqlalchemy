from sqlalchemy import (
    Column, BigInteger, Integer, String, Date, PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship, remote, foreign

from .base import Base
from .audit_entity import AuditEntity

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
    season = relationship("Season",
        primaryjoin="remote(Season.id)==foreign(DraftPick.season_id)"
    )
    team = relationship("Team",
        primaryjoin="remote(Team.id)==foreign(DraftPick.team_id)"
    )
    player = relationship("Player",
        primaryjoin="remote(Player.id)==foreign(DraftPick.player_id)"
    )

    def __repr__(self):
        return (
            "<DraftPick("
                "player='{}', "
                "overall_pick='{}', "
                "team='{}', "
                "season='{}'"
            ")>".format(
                self.player.name, 
                self.overall_pick, 
                self.team.abbreviation, 
                self.season.pretty_print_years()
            )
        )
