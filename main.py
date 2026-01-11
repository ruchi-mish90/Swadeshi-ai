import json
from core.engine import TradeoffEngine
from core.models import TechOption
import sys
from kiro.tester import TestTradeoffEngine
from kiro.profiler import profile_engine

def run_architect():
    print("=== Welcome to The Trade-Off Architect ===")
    
    # Load Data
    with open('data/technologies.json') as f:
        data = json.load(f)
    
    # Map JSON keys to expected metric keys and create TechOption objects
    tech_options = []
    for tech_data in data['database_comparison']:
        metrics = {
            "speed": tech_data["speed_of_setup"],
            "reliability": tech_data["relational_power"],
            "cost": tech_data["cost_at_scale"]
        }
        tech_option = TechOption(
            name=tech_data["name"],
            metrics=metrics,
            tradeoff_note=tech_data["tradeoff_note"]
        )
        tech_options.append(tech_option)
    
    # 1. Ask for Constraints (Weights)
    print("\nRank importance (1-5) for your project:")
    speed_w = int(input("How important is Speed-to-Market? "))
    reliability_w = int(input("How important is Relational Data? "))
    cost_w = int(input("How important is Cost Efficiency? "))

    weights = {
        "speed": speed_w,
        "reliability": reliability_w,
        "cost": cost_w
    }

    # 2. Process Trade-offs
    engine = TradeoffEngine(tech_options)
    rankings = engine.calculate_best_fit(weights)

    # 3. Present the Decision
    winner = rankings[0]
    runner_up = rankings[1]

    print("\n--- THE VERDICT ---")
    print(f"🏆 RECOMMENDED: {winner.name} (Score: {winner.total_score})")
    print(f"💡 WHY: {winner.tradeoff_note}")
    print(f"\n❌ THE TRADE-OFF: By choosing {winner.name}, you are deprioritizing {runner_up.name}'s strength in " + 
          ("relational power" if speed_w < reliability_w else "setup speed") + ".")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            import unittest
            suite = unittest.TestLoader().loadTestsFromModule(TestTradeoffEngine)
            unittest.TextTestRunner(verbosity=2).run(suite)
        elif sys.argv[1] == "--profile":
            profile_engine()
        else:
            print("Usage: python main.py [--test | --profile]")
    else:
        run_architect()