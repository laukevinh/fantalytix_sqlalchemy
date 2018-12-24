import unittest

from datetime import datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common.player_url import PlayerUrl
from fantalytix_sqlalchemy.test.settings import CONNECTION

class TestPlayerUrlORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_player_url(self):
        LBJ_URL = PlayerUrl(
            player_id=1,
            url='https://www.basketball-reference.com/players/j/jamesle01.html', 
            site='basketball-reference',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(LBJ_URL)
        test_player_url = self.session.query(PlayerUrl).filter_by(url='https://www.basketball-reference.com/players/j/jamesle01.html')
        self.assertTrue(LBJ_URL is test_player_url.first())

if __name__ == '__main__':
    unittest.main()
