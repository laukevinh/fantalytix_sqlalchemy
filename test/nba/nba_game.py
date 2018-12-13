import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine, Date, cast
from sqlalchemy.orm import sessionmaker

from orm.nba.nba_game import NBAGame
from test.settings import CONNECTION

class TestNBAGameORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(NBAGame).delete()
        self.session.commit()
        self.session.close()

    def test_nba_game(self):
        CLE_GSW_2018_12_05 = NBAGame(
            season='2018-19',
            home_team_id=2,
            away_team_id=1,
            game_date=datetime(2018, 12, 5, 19, 0, 0, tzinfo=timezone.utc),
            home_score=105,
            away_score=129,
            overtimes=0,
            winning_team_id=1,
            status='scheduled',
            type='season',
            created_by='pycrawl',
            creation_date=datetime(2018, 12, 5, 19, 0, 0, tzinfo=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )

        self.session.add(CLE_GSW_2018_12_05)

        test_game = self.session.query(NBAGame).filter(
            cast(NBAGame.game_date, Date)==date(2018, 12, 5))
        self.assertTrue(CLE_GSW_2018_12_05 is test_game.first())

        self.session.commit()

if __name__ == '__main__':
    unittest.main()
