import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_success(self):
        self.assertEqual(self.stats.search("Semenko").name, "Semenko")

    def test_search_failure(self):
        self.assertEqual(self.stats.search("Me"), None)

    def test_team_filter(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)

    def test_top_points_default(self):
        top1 = self.stats.top(how_many=1)
        self.assertEqual(len(top1), 1)
        self.assertEqual(top1[0].name, "Gretzky")

    def test_top_goals(self):
        top2 = self.stats.top(how_many=2, field=SortBy.GOALS)
        self.assertEqual(len(top2), 2)
        self.assertEqual(top2[0].name, "Lemieux")

    def test_top_assists(self):
        top3 = self.stats.top(how_many=3, field=SortBy.ASSISTS)
        self.assertEqual(len(top3), 3)
        self.assertEqual(top3[0].name, "Gretzky")
