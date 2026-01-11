from core.models import TechOption, ComparisonResult
from typing import List, Dict

class TradeoffEngine:
    def __init__(self, tech_list: List[TechOption]):
        self.options = tech_list

    def calculate_best_fit(self, user_weights: Dict[str, int]) -> List[ComparisonResult]:
        rankings = []
        for tech in self.options:
            score = 0
            for criteria, weight in user_weights.items():
                score += tech.get_metric(criteria) * weight
            
            rankings.append(ComparisonResult(
                name=tech.name,
                total_score=score,
                tradeoff_note=tech.tradeoff_note
            ))
        
        # Sort results
        sorted_results = sorted(rankings, key=lambda x: x.total_score, reverse=True)
        
        # Mark the winner
        if sorted_results:
            sorted_results[0].is_winner = True
            
        return sorted_results