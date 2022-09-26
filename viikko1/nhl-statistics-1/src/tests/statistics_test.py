import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_returns_correct(self):
        self.assertEqual(self.statistics.search(
            "Kurri").__str__(), "Kurri EDM 37 + 53 = 90")

    def test_search_returns_none(self):
        self.assertEqual(self.statistics.search("Kulli"), None)

    def test_team_returns_correct_list(self):
        correct_list = [Player("Semenko", "EDM", 4, 12),
                        Player("Kurri", "EDM", 37, 53),
                        Player("Gretzky", "EDM", 35, 89)]

        team_players = self.statistics.team("EDM")

        result = False
        for i in range(0,2):
            if correct_list[i].__str__() == team_players[i].__str__():
                result = True
            else:
                result = False

        self.assertTrue(result)

    def test_top_scorers_returns_correct(self):
        top_scorers = self.statistics.top_scorers(3)
        correct = [Player("Gretzky", "EDM", 35, 89), Player("Lemieux", "PIT", 45, 54), Player("Yzerman", "DET", 42, 56)]
        
        result = False
        for i in range(0,2):
            if correct[i].__str__() == top_scorers[i].__str__():
                result = True
            else:
                result = False

        self.assertTrue(result)