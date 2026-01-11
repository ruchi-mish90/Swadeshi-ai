from core.models import TechOption

def generate_tech_option(name, speed, reliability, cost, note):
    """Generates a TechOption instance."""
    metrics = {"speed": speed, "reliability": reliability, "cost": cost}
    return TechOption(name=name, metrics=metrics, tradeoff_note=note)

# Example usage
if __name__ == "__main__":
    new_tech = generate_tech_option("KiroTech", 4, 4, 3, "Accelerated by Kiro")
    print(f"Generated: {new_tech.name}")