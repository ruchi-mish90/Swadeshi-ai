#!/usr/bin/env python3
"""
Demo script to showcase the Trade-Off Architect in action.
This simulates user input for demonstration purposes.
"""

import json
from core.engine import TradeoffEngine
from core.models import TechOption
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def demo_architect():
    print("=== Welcome to The Trade-Off Architect ===")
    print("🚀 Making tech decisions with data, not vibes!\n")
    
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
    
    # Demo scenario: Startup prioritizing speed-to-market
    print("\n🎯 Demo Scenario: Early-stage startup prioritizing rapid deployment")
    print("Simulating user input:")
    
    speed_w = 5
    reliability_w = 2
    cost_w = 4
    
    print(f"How important is Speed-to-Market? (1-5): {speed_w}")
    print(f"How important is Relational Data? (1-5): {reliability_w}")
    print(f"How important is Cost Efficiency? (1-5): {cost_w}")

    weights = {
        "speed": speed_w,
        "reliability": reliability_w,
        "cost": cost_w
    }

    # Process Trade-offs
    engine = TradeoffEngine(tech_options)
    rankings = engine.calculate_best_fit(weights)

    # Present the Decision with Enhanced Analysis
    print("\n" + "="*50)
    print(engine.get_trade_off_analysis(rankings))
    print("="*50)
    
    # Show all rankings
    print("\n📈 COMPLETE RANKINGS:")
    for i, result in enumerate(rankings, 1):
        status = "🏆" if result.is_winner else f"{i}."
        print(f"{status} {result.name}: {result.total_score}%")
    
    print("\n✨ Decision made with data-driven analysis!")
    print("🎯 The Trade-Off Architect helps you understand the implications of your choice.")

if __name__ == "__main__":
    demo_architect()