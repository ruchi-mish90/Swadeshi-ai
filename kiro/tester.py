import unittest
from core.models import TechOption, ComparisonResult
from core.engine import TradeoffEngine

class TestTradeoffEngine(unittest.TestCase):
    def setUp(self):
        self.tech1 = TechOption(name="TestTech1", metrics={"speed": 5, "reliability": 3, "cost": 2}, tradeoff_note="Test note")
        self.tech2 = TechOption(name="TestTech2", metrics={"speed": 2, "reliability": 5, "cost": 4}, tradeoff_note="Another note")
        self.engine = TradeoffEngine([self.tech1, self.tech2])

    def test_calculate_best_fit(self):
        weights = {"speed": 1, "reliability": 1, "cost": 1}
        rankings = self.engine.calculate_best_fit(weights)
        self.assertEqual(len(rankings), 2)
        self.assertGreater(rankings[0].total_score, rankings[1].total_score)

if __name__ == "__main__":
    unittest.main()