"""
Quick start guide and example usage
"""

def main():
    import streamlit as st
    from utils import DataManager, InsightGenerator
    
    st.title("UCL Analytics - Quick Start Example")
    
    # Initialize managers
    data_manager = DataManager()
    insight_generator = InsightGenerator()
    
    # Example: Get team stats
    team = "Manchester City"
    team_stats = data_manager.get_team_stats(team)
    
    st.write(f"Team: {team_stats.team_name}")
    st.write(f"Goals: {team_stats.goals}")
    st.write(f"Expected Goals: {team_stats.expected_goals}")
    st.write(f"Possession: {team_stats.possession}%")
    
    # Example: Generate insights
    insights = insight_generator.generate_team_insights(team_stats)
    st.write("Insights:")
    for key, value in insights.items():
        st.write(f"- {key}: {value}")

if __name__ == "__main__":
    main()
