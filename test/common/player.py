import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm.common.player import Player
from test.settings import CONNECTION

class TestPlayerORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_player(self):
        LBJ = Player(
            name='LeBron James',
            height = '6-8',
            weight = 250,
            birthday = date(1984, 12, 30),
            birthplace = 'in Akron, Ohio',
            nationality = 'us',
            created_by='pycrawl',
            creation_date=datetime(2018, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            last_updated_by='pycrawl',
            last_updated_date=datetime(2018, 2, 2, 0, 0, 0, tzinfo=timezone.utc)
        )
        self.session.add(LBJ)
        test_player = self.session.query(Player).filter_by(name='LeBron James')
        self.assertTrue(LBJ is test_player.first())

if __name__ == '__main__':
    unittest.main()
