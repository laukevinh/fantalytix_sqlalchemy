import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common.player import Player
from ..settings import CONNECTION

class TestPlayerORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_player(self):
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
        self.assertIs(self.session.query(Player).one(), player)

if __name__ == '__main__':
    unittest.main()
