# Design for Trade-Off Architect

## Architecture
- **main.py**: Entry point for user interaction, data loading, engine call.
- **core/models.py**: Dataclasses for TechOption and ComparisonResult.
- **core/engine.py**: TradeoffEngine class for scoring and ranking.
- **data/technologies.json**: Sample tech data.
- **kiro/**: Acceleration module (tester, generator, profiler).

## Workflow
1. Load data.
2. Get weights.
3. Process rankings.
4. Output verdict.