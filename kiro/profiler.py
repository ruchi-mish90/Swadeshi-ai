import cProfile
from core.engine import TradeoffEngine
from core.models import TechOption

def profile_engine():
    cProfile.run('''
from core.engine import TradeoffEngine
from core.models import TechOption
techs = [
    TechOption(name="Tech1", metrics={"speed": 5, "reliability": 3, "cost": 2}, tradeoff_note="Note1"),
    TechOption(name="Tech2", metrics={"speed": 2, "reliability": 5, "cost": 4}, tradeoff_note="Note2")
]
engine = TradeoffEngine(techs)
weights = {"speed": 1, "reliability": 1, "cost": 1}
engine.calculate_best_fit(weights)
''')

if __name__ == "__main__":
    profile_engine()