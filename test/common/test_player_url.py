import unittest

from datetime import datetime, timezone, date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common import Player
from fantalytix_sqlalchemy.orm.common import PlayerUrl
from ..settings import CONNECTION

class TestPlayerUrlORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(Player).delete()
        self.session.query(PlayerUrl).delete()
        self.session.commit()
        self.session.close()

    def test_player_url(self):
        player = Player(
            name='LeBron James',
            height = '6-8',
            weight = 250,
            birthday = date(1984, 12, 30),
            birthplace = 'in Akron, Ohio',
            nationality = 'us',
            created_by='pycrawl',
        )
        self.session.add(player)
        self.session.commit()

        player_url = PlayerUrl(
            player=player,
            url='https://www.basketball-reference.com/players/j/jamesle01.html', 
            site='basketball-reference',
            created_by='pycrawl',
        )
        self.session.add(player_url)
        self.session.commit()

        self.assertIs(
            self.session.query(PlayerUrl).one().player,
            self.session.query(Player).one()
        )

if __name__ == '__main__':
    unittest.main()
