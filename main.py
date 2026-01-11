import json
from core.engine import TradeoffEngine
from core.models import TechOption
import sys
import logging
from kiro.tester import TestTradeoffEngine
from kiro.profiler import profile_engine

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def run_architect():
    print("=== Welcome to The Trade-Off Architect ===")
    print("🚀 Making tech decisions with data, not vibes!\n")
    
    try:
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
        
        print(f"📊 Loaded {len(tech_options)} technology options for comparison")
        for tech in tech_options:
            print(f"   • {tech.name}")
        
        # 1. Ask for Constraints (Weights)
        print("\n🎯 Rank importance (1-5) for your project:")
        speed_w = int(input("How important is Speed-to-Market? (1-5): "))
        reliability_w = int(input("How important is Relational Data? (1-5): "))
        cost_w = int(input("How important is Cost Efficiency? (1-5): "))

        weights = {
            "speed": speed_w,
            "reliability": reliability_w,
            "cost": cost_w
        }

        # 2. Process Trade-offs
        engine = TradeoffEngine(tech_options)
        rankings = engine.calculate_best_fit(weights)

        # 3. Present the Decision with Enhanced Analysis
        print("\n" + "="*50)
        print(engine.get_trade_off_analysis(rankings))
        print("="*50)
        
        # Show all rankings
        print("\n📈 COMPLETE RANKINGS:")
        for i, result in enumerate(rankings, 1):
            status = "🏆" if result.is_winner else f"{i}."
            print(f"{status} {result.name}: {result.total_score}%")
            
    except FileNotFoundError:
        print("❌ Error: Could not find technologies.json file")
        print("Make sure you're running from the project root directory")
    except ValueError as e:
        print(f"❌ Input Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            print("🧪 Running test suite...")
            import unittest
            from kiro.tester import TestTradeoffEngine
            suite = unittest.TestLoader().loadTestsFromTestCase(TestTradeoffEngine)
            unittest.TextTestRunner(verbosity=2).run(suite)
        elif sys.argv[1] == "--profile":
            print("⚡ Running performance profiler...")
            profile_engine()
        else:
            print("Usage: python main.py [--test | --profile]")
    else:
        run_architect()