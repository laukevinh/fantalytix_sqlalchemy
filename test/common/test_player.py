import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common.player import Player
from fantalytix_sqlalchemy.test.settings import CONNECTION

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
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(LBJ)
        test_player = self.session.query(Player).filter_by(name='LeBron James')
        self.assertTrue(LBJ is test_player.first())

if __name__ == '__main__':
    unittest.main()
