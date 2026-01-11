from dataclasses import dataclass
from typing import Dict

@dataclass
class TechOption:
    name: str
    metrics: Dict[str, int]
    tradeoff_note: str

    def get_metric(self, key: str) -> int:
        return self.metrics[key]

@dataclass
class ComparisonResult:
    name: str
    total_score: int
    tradeoff_note: str
    is_winner: bool = False