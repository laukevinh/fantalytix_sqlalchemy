from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, BigInteger, Integer, String, Date

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    __table_args__ = {'schema':'fantalytix'}

    # Add sequence

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    height = Column(String(7))
    weight = Column(Integer)
    birthday = Column(Date)
    birthplace = Column(String(100))
    nationality = Column(String(50))

    def __repr__(self):
        return "<Player(name='{name}')>".format(name = self.name)

class PlayerUrl(Base):
    __tablename__ = 'player_urls'
    __table_args__ = {'schema':'fantalytix'}

    player_id = Column(BigInteger, nullable=False)
    url = Column(String(512), primary_key=True, nullable=False)
    site = Column(String(50), nullable=False)

    def __repr__(self):
        return "<PlayerUrl(url='{url}')>".format(url=self.url[:10])
