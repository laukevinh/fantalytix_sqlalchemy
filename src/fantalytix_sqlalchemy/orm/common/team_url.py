from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

from fantalytix_sqlalchemy.orm.common.audit_entity import AuditEntity

Base = declarative_base()

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

    def __repr__(self):
        return "<Team(name='{}')>".format(self.name)
