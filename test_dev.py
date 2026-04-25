"""
Development and testing utilities
"""
import json
from utils import DataManager, InsightGenerator
from datetime import datetime

def test_data_manager():
    """Test data manager functionality"""
    print("Testing DataManager...")
    dm = DataManager()
    
    teams = ["Manchester City", "Real Madrid", "Bayern Munich"]
    
    for team in teams:
        stats = dm.get_team_stats(team)
        print(f"\n{team}:")
        print(f"  Goals: {stats.goals} (xG: {stats.expected_goals})")
        print(f"  Goals Conceded: {stats.goals_conceded} (xGA: {stats.expected_goals_conceded})")
        print(f"  Possession: {stats.possession}%")

def test_insight_generator():
    """Test insight generator"""
    print("\n\nTesting InsightGenerator...")
    dm = DataManager()
    ig = InsightGenerator()
    
    team = "Manchester City"
    stats = dm.get_team_stats(team)
    
    insights = ig.generate_team_insights(stats)
    print(f"\n{team} Insights:")
    for key, value in insights.items():
        print(f"  {key}: {value}")
    
    bullets = ig.generate_summary_bullets(stats)
    print(f"\nSummary Bullets:")
    for bullet in bullets:
        print(f"  {bullet}")

def test_all():
    """Run all tests"""
    print("="*50)
    print("UCL Analytics - Development Tests")
    print("="*50)
    print(f"Test started: {datetime.now()}")
    print()
    
    test_data_manager()
    test_insight_generator()
    
    print("\n" + "="*50)
    print("All tests completed successfully!")
    print("="*50)

if __name__ == "__main__":
    test_all()
