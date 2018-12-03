import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm.common.player import Player, PlayerUrl
from orm.settings import CONNECTION

class TestPlayerORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_player(self):
        LBJ = Player(name='LeBron James')
        self.session.add(LBJ)
        test_player = self.session.query(Player).filter_by(name='LeBron James')
        self.assertTrue(LBJ is test_player.first())

    def test_player_url(self):
        LBJ_URL = PlayerUrl(
            player_id=1,
            url='https://www.basketball-reference.com/players/j/jamesle01.html', 
            site='basketball-reference'
        )
        self.session.add(LBJ_URL)
        test_player_url = self.session.query(PlayerUrl).filter_by(url='https://www.basketball-reference.com/players/j/jamesle01.html')
        self.assertTrue(LBJ_URL is test_player_url.first())

if __name__ == '__main__':
    unittest.main()
