from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, remote, foreign

from .base import Base
from .audit_entity import AuditEntity

class TeamUrl(Base, AuditEntity):
    __tablename__ = 'team_urls'
    __table_args__ = {'schema':'fantalytix'}
    __table_args__ = (
        PrimaryKeyConstraint(
            'team_id',
            'site', 
            name='team_urls_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    team_id = Column(Integer, nullable=False)
    site = Column(String(50), nullable=False)
    url = Column(String(512), unique=True, nullable=False)
    team = relationship("Team",
        primaryjoin="remote(Team.id)==foreign(TeamUrl.team_id)"
    )

    def __repr__(self):
        return "<TeamUrl(team='{}', site='{}')>".format(
            self.team.abbreviation, self.site
        )
