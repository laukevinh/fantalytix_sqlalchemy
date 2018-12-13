import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine, Date, cast
from sqlalchemy.orm import sessionmaker

from orm.nba.nba_game_url import NBAGameUrl
from test.settings import CONNECTION

class TestNBAGameUrlORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(NBAGameUrl).delete()
        self.session.commit()
        self.session.close()

    def test_nba_game_url(self):
        CLE_GSW_2018_12_05 = NBAGameUrl(
            nba_game_id=1,
            url = ('https://www.basketball-reference.com/'
                   'boxscores/201812050CLE.html'),
            site = 'basketball-reference',
            created_by='pycrawl',
            creation_date=datetime(2018, 12, 5, 19, 0, 0, tzinfo=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )

        self.session.add(CLE_GSW_2018_12_05)

        test_game = self.session.query(NBAGameUrl).filter_by(
            url=('https://www.basketball-reference.com/'
                 'boxscores/201812050CLE.html'))
        self.assertTrue(CLE_GSW_2018_12_05 is test_game.first())

        self.session.commit()

if __name__ == '__main__':
    unittest.main()
