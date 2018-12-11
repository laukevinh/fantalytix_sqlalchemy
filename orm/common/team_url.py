from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

from orm.common.audit_entity import AuditEntity

Base = declarative_base()

class TeamUrl(Base, AuditEntity):
    __tablename__ = 'team_urls'
    __table_args__ = {'schema':'fantalytix'}

    team_id = Column(Integer, nullable=False)
    url = Column(String(512), primary_key=True, nullable=False)
    site = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Team(name='{}')>".format(self.name)
