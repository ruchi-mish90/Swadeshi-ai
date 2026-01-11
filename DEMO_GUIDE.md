# Trade-Off Architect - Kiro Demonstration Guide

This guide shows how to capture the three key screenshots demonstrating Kiro's capabilities with your Trade-Off Architect project.

## 📋 Screenshot 1: Structured Planning (Kiro Task List)

**What to show**: The structured breakdown of engineering tasks using Kiro's planning capabilities.

**How to capture**:
1. Open the Kiro IDE with your project
2. Navigate to the `.kiro/tasks.md` file to show the structured task breakdown
3. Optionally show the Agent Hooks panel if available in your Kiro version
4. The screenshot should show:
   - Task breakdown with phases (Foundation, Core Implementation, Quality & Performance, Enhancement)
   - Checkboxes showing completed vs. pending tasks
   - Kiro automation hooks for testing and profiling

**Key elements visible**:
- ✅ Completed tasks (Phases 1 & 2)
- 🔄 In-progress tasks (Phase 3)
- 📝 Future enhancements (Phase 4)
- 🔧 Kiro automation hooks

## 💻 Screenshot 2: Development Process (Code + Kiro Interface)

**What to show**: Enhanced TradeoffEngine code alongside Kiro's AI assistance interface.

**How to capture**:
1. Open `core/engine.py` in the Kiro editor
2. Show the enhanced version with:
   - Comprehensive docstrings
   - Error handling and validation
   - Logging integration
   - Trade-off analysis methods
3. Have Kiro chat panel visible showing AI assistance
4. Optionally show diagnostics or suggestions from Kiro

**Key elements visible**:
- Enhanced `TradeoffEngine` class with professional code structure
- Kiro AI chat interface providing development assistance
- Code improvements like error handling, logging, and documentation
- Kiro's intelligent code suggestions and analysis

## 🚀 Screenshot 3: Tool in Action (Terminal Output)

**What to show**: The Trade-Off Architect running and providing technical recommendations.

**How to capture**:
1. Run the demo script: `python demo_run.py`
2. Capture the terminal output showing:
   - Welcome message and loaded technologies
   - Simulated user input (weights for criteria)
   - Data-driven recommendation with detailed analysis
   - Complete rankings and trade-off explanations

**Commands to run**:
```bash
# Navigate to project directory
cd tradeoff_architect

# Run the demo (shows complete output)
python demo_run.py

# Alternative: Run tests to show quality assurance
python main.py --test

# Alternative: Run profiler to show performance analysis
python main.py --profile
```

**Key elements visible**:
- 🚀 Professional welcome message
- 📊 Technology options loaded from data
- 🎯 User input simulation (startup scenario)
- 🏆 Data-driven recommendation with percentage scores
- 📈 Complete rankings showing all options
- 🤔 Trade-off analysis explaining the decision

## 🎯 Demo Scenarios

### Scenario 1: Speed-Focused Startup
- Speed: 5, Reliability: 2, Cost: 4
- Expected winner: Firebase or PlanetScale
- Shows prioritizing rapid deployment

### Scenario 2: Enterprise Application
- Speed: 2, Reliability: 5, Cost: 3
- Expected winner: Supabase (PostgreSQL)
- Shows prioritizing data integrity

### Scenario 3: Cost-Conscious Project
- Speed: 3, Reliability: 3, Cost: 5
- Expected winner: PlanetScale (MySQL)
- Shows balancing features with budget

## 📝 Screenshot Composition Tips

1. **Structured Planning**: Focus on the task breakdown and show how Kiro helps organize complex projects
2. **Development Process**: Split screen showing code and Kiro interface to demonstrate AI-assisted development
3. **Tool in Action**: Full terminal output showing the professional, data-driven decision-making process

Each screenshot should clearly demonstrate how Kiro enhances the development workflow from planning through implementation to execution.