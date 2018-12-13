from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, Integer, 
    String, DateTime)

from orm.common.audit_entity import AuditEntity

Base = declarative_base()

class NBAGameUrl(Base, AuditEntity):
    __tablename__ = 'nba_game_urls'
    __table_args__ = {'schema':'fantalytix'}

    nba_game_id = Column(BigInteger, nullable=False)
    url = Column(String(512), nullable=False, primary_key=True)
    site = Column(String(50), nullable=False)

    def __repr__(self):
        return "<NBAGameUrl(site={}, creation_date='{}')>".format(
            self.home_team_id, self.game_date.strftime('%Y/%m/%d'))
