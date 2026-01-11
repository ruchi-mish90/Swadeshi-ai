from core.models import TechOption, ComparisonResult
from typing import List, Dict, Optional
import logging

class TradeoffEngine:
    """
    A weighted decision matrix engine for comparing technology options.
    
    This engine calculates scores based on user-defined weights and provides
    detailed trade-off analysis to help developers make informed decisions.
    """
    
    def __init__(self, tech_list: List[TechOption]):
        self.options = tech_list
        self.logger = logging.getLogger(__name__)
        
    def calculate_best_fit(self, user_weights: Dict[str, int]) -> List[ComparisonResult]:
        """
        Calculate weighted scores for all technology options.
        
        Args:
            user_weights: Dictionary mapping criteria to importance weights (1-5)
            
        Returns:
            List of ComparisonResult objects sorted by total score (highest first)
        """
        if not user_weights:
            raise ValueError("User weights cannot be empty")
            
        rankings = []
        max_possible_score = sum(user_weights.values()) * 5  # Max metric value is 5
        
        for tech in self.options:
            score = self._calculate_weighted_score(tech, user_weights)
            normalized_score = (score / max_possible_score) * 100  # Convert to percentage
            
            rankings.append(ComparisonResult(
                name=tech.name,
                total_score=round(normalized_score, 1),
                tradeoff_note=tech.tradeoff_note
            ))
        
        # Sort results by score (highest first)
        sorted_results = sorted(rankings, key=lambda x: x.total_score, reverse=True)
        
        # Mark the winner
        if sorted_results:
            sorted_results[0].is_winner = True
            self.logger.info(f"Winner: {sorted_results[0].name} with score {sorted_results[0].total_score}")
            
        return sorted_results
    
    def _calculate_weighted_score(self, tech: TechOption, weights: Dict[str, int]) -> float:
        """Calculate the weighted score for a single technology option."""
        score = 0
        for criteria, weight in weights.items():
            metric_value = tech.get_metric(criteria)
            score += metric_value * weight
        return score
    
    def get_trade_off_analysis(self, results: List[ComparisonResult]) -> str:
        """
        Generate a detailed trade-off analysis comparing top options.
        
        Args:
            results: Sorted list of ComparisonResult objects
            
        Returns:
            Formatted string with trade-off insights
        """
        if len(results) < 2:
            return "Insufficient options for trade-off analysis."
            
        winner = results[0]
        runner_up = results[1]
        score_gap = winner.total_score - runner_up.total_score
        
        analysis = f"""
🏆 RECOMMENDED: {winner.name} (Score: {winner.total_score}%)
💡 WHY: {winner.tradeoff_note}

🥈 RUNNER-UP: {runner_up.name} (Score: {runner_up.total_score}%)
📊 SCORE GAP: {score_gap:.1f} percentage points

🤔 TRADE-OFF CONSIDERATION:
By choosing {winner.name}, you're prioritizing the criteria you weighted most heavily.
However, {runner_up.name} might excel in areas you weighted lower.
"""
        return analysis