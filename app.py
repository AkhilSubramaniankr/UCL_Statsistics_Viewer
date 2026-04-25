"""
UCL Elite Analytics Platform - Main Streamlit Application
"""
import streamlit as st
from utils import DataManager, InsightGenerator, UIComponents
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize page configuration
UIComponents.setup_page_config()

# Initialize session state
if 'selected_team' not in st.session_state:
    st.session_state.selected_team = "Manchester City"

# Initialize managers
data_manager = DataManager()
insight_generator = InsightGenerator()

# Header
st.markdown("""
<div style='text-align: center; padding: 30px 0;'>
    <h1 style='color: #004d99; font-size: 48px; margin: 0;'>⚽ UCL ELITE ANALYTICS</h1>
    <p style='color: #ff6b00; font-size: 18px; margin-top: 5px;'>Champions League Performance Intelligence Platform</p>
    <div style='height: 3px; background: linear-gradient(90deg, #004d99, #ff6b00); margin: 20px 0;'></div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Platform Settings")
    
    # Team selector
    teams = ["Manchester City", "Real Madrid", "Bayern Munich", "PSG", "Inter Milan", "Liverpool", "Arsenal"]
    selected_team = st.selectbox(
        "Select Team:",
        teams,
        index=teams.index(st.session_state.selected_team) if st.session_state.selected_team in teams else 0
    )
    st.session_state.selected_team = selected_team
    
    # Refresh button
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 Platform Info")
    st.info(
        """
        **UCL Elite Analytics**
        
        Real-time performance analytics and AI-powered insights for UEFA Champions League teams.
        
        📱 Features:
        - Live team statistics
        - Player performance tracking
        - Injury management
        - AI tactical analysis
        - Broadcast-quality insights
        """
    )

# Tabs for different sections
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📊 Overview", "👥 Players", "🏥 Injuries", "📋 Matches", "🧠 Insights"]
)

try:
    # Fetch data
    team_stats = data_manager.get_team_stats(selected_team)
    player_stats = data_manager.get_player_stats(selected_team)
    injury_reports = data_manager.get_injury_reports(selected_team)
    recent_matches = data_manager.get_recent_matches(selected_team)
    
    if not team_stats:
        st.error("Unable to fetch team data. Please check your API configuration.")
        st.stop()
    
    # TAB 1: OVERVIEW
    with tab1:
        st.markdown("### Key Metrics")
        UIComponents.render_key_metrics_card(team_stats)
        
        UIComponents.render_team_overview(team_stats)
    
    # TAB 2: PLAYERS
    with tab2:
        UIComponents.render_player_stats_panel(player_stats)
    
    # TAB 3: INJURIES
    with tab3:
        UIComponents.render_injury_report(injury_reports)
    
    # TAB 4: MATCHES
    with tab4:
        UIComponents.render_recent_matches(recent_matches)
    
    # TAB 5: AI INSIGHTS
    with tab5:
        # Generate insights
        insights = insight_generator.generate_team_insights(team_stats)
        summary_bullets = insight_generator.generate_summary_bullets(team_stats)
        
        UIComponents.render_insights_panel(insights)
        
        st.markdown("---")
        
        UIComponents.render_summary_panel(summary_bullets, selected_team)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.info("Please check your configuration and ensure all required API keys are set in the .env file.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 12px; padding: 20px 0;'>
    <p>UCL Elite Analytics Platform © 2024 | Powered by Streamlit, OpenAI & Football Data APIs</p>
    <p>For support, please check the documentation or contact the development team.</p>
</div>
""", unsafe_allow_html=True)
