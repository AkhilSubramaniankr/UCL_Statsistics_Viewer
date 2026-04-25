"""
Sky Sports style UI components and visualizations
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict
from .models import TeamStats, PlayerStats, InjuryReport, Match
from datetime import datetime

class UIComponents:
    """Sky Sports themed UI components"""
    
    # Color scheme - Sky Sports style (Dark theme)
    PRIMARY_COLOR = "#004d99"  # Sky blue
    SECONDARY_COLOR = "#1a1a2e"  # Dark gray
    ACCENT_COLOR = "#ff6b00"  # Orange accent
    TEXT_COLOR = "#ffffff"  # White text
    GRID_COLOR = "#2a2a3e"
    
    @staticmethod
    def setup_page_config():
        """Setup Streamlit page configuration"""
        st.set_page_config(
            page_title="UCL Elite Analytics",
            page_icon="⚽",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Custom CSS for Sky Sports theme
        st.markdown("""
        <style>
            * {
                font-family: 'Segoe UI', 'Trebuchet MS', sans-serif;
            }
            
            body {
                background-color: #0f0f1e;
                color: #ffffff;
            }
            
            .main {
                background-color: #0f0f1e;
            }
            
            .st-emotion-cache-1y4p8pa {
                background-color: #1a1a2e;
                border: 2px solid #004d99;
            }
            
            /* Card styling */
            div[data-testid="metric-container"] {
                background-color: #1a1a2e;
                border: 2px solid #004d99;
                border-radius: 8px;
                padding: 15px;
                box-shadow: 0 4px 6px rgba(0, 77, 153, 0.2);
            }
            
            /* Header styling */
            h1, h2, h3 {
                color: #ffffff;
                text-shadow: 0 0 10px rgba(0, 77, 153, 0.5);
            }
            
            .highlight-text {
                color: #ff6b00;
                font-weight: bold;
            }
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_key_metrics_card(team_stats: TeamStats):
        """Render key metrics in Sky Sports style cards"""
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        with col1:
            st.metric("⚽ Goals", f"{int(team_stats.goals)}", 
                     f"+{team_stats.goals - team_stats.expected_goals:.1f}")
        
        with col2:
            st.metric("🎯 xG", f"{team_stats.expected_goals:.1f}")
        
        with col3:
            st.metric("🛡️ Goals Conceded", f"{int(team_stats.goals_conceded)}")
        
        with col4:
            st.metric("⛔ xGA", f"{team_stats.expected_goals_conceded:.1f}")
        
        with col5:
            st.metric("👥 Possession", f"{team_stats.possession:.1f}%")
        
        with col6:
            st.metric("✓ Clean Sheets", f"{team_stats.clean_sheets}")
    
    @staticmethod
    def render_team_overview(team_stats: TeamStats):
        """Render team overview panel"""
        st.markdown("---")
        st.subheader(f"📊 Team Overview: {team_stats.team_name}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Attacking metrics chart
            fig_attacking = go.Figure()
            categories = ['Goals', 'xG', 'Goals Conceded', 'xGA']
            values = [
                team_stats.goals,
                team_stats.expected_goals,
                team_stats.goals_conceded,
                team_stats.expected_goals_conceded
            ]
            
            fig_attacking = go.Figure(data=[
                go.Bar(x=categories[:2], y=values[:2], name='Attacking', marker_color='#004d99'),
                go.Bar(x=categories[2:], y=values[2:], name='Defensive', marker_color='#ff6b00'),
            ])
            
            fig_attacking.update_layout(
                title="Goals vs xG Performance",
                template="plotly_dark",
                plot_bgcolor='#1a1a2e',
                paper_bgcolor='#0f0f1e',
                font=dict(color='#ffffff'),
                barmode='group',
                height=350
            )
            st.plotly_chart(fig_attacking, use_container_width=True)
        
        with col2:
            # Match statistics
            fig_stats = go.Figure()
            
            fig_stats = go.Figure(data=[
                go.Scatterpolar(
                    r=[
                        (team_stats.goals / 3) * 100,  # Normalize to 0-100
                        (team_stats.possession),
                        (team_stats.clean_sheets / team_stats.matches) * 100,
                        min((team_stats.expected_goals / team_stats.matches) * 100, 100)
                    ],
                    theta=['Goals/Match', 'Possession', 'Clean Sheet %', 'xG/Match'],
                    fill='toself',
                    name='Team Stats',
                    line=dict(color='#004d99'),
                    fillcolor='rgba(0, 77, 153, 0.3)'
                )
            ])
            
            fig_stats.update_layout(
                title="Radar Chart - Performance Metrics",
                template="plotly_dark",
                plot_bgcolor='#1a1a2e',
                paper_bgcolor='#0f0f1e',
                font=dict(color='#ffffff'),
                height=350
            )
            st.plotly_chart(fig_stats, use_container_width=True)
    
    @staticmethod
    def render_player_stats_panel(players: List[PlayerStats]):
        """Render player statistics panel"""
        st.markdown("---")
        st.subheader("👥 Top Players")
        
        # Create dataframe for display
        player_data = []
        for p in players:
            player_data.append({
                "Player": p.player_name,
                "Position": p.position,
                "Goals": p.goals,
                "Assists": p.assists,
                "xG": f"{p.expected_goals:.2f}",
                "Minutes": p.minutes_played,
                "Shots": p.shots
            })
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.dataframe(
                player_data,
                use_container_width=True,
                hide_index=True,
            )
        
        with col2:
            # Top scorer
            if players:
                top_scorer = max(players, key=lambda x: x.goals)
                st.markdown(f"""
                <div style='background-color: #1a1a2e; padding: 20px; border-radius: 8px; 
                border-left: 4px solid #004d99;'>
                    <h4 style='color: #ff6b00;'>⭐ Top Scorer</h4>
                    <p style='font-size: 24px; font-weight: bold;'>{top_scorer.player_name}</p>
                    <p style='color: #004d99;'>{top_scorer.goals} Goals • {top_scorer.assists} Assists</p>
                </div>
                """, unsafe_allow_html=True)
    
    @staticmethod
    def render_injury_report(injuries: List[InjuryReport]):
        """Render injury report"""
        st.markdown("---")
        st.subheader("🏥 Injury Report")
        
        if not injuries:
            st.info("✓ No current injuries reported")
            return
        
        for injury in injuries:
            status_color = "🔴" if injury.status == "Out" else "🟡"
            
            st.markdown(f"""
            <div style='background-color: #1a1a2e; padding: 15px; border-radius: 8px; 
            border-left: 4px solid #ff6b00; margin-bottom: 10px;'>
                <h4>{status_color} {injury.player_name}</h4>
                <p><strong>Injury:</strong> {injury.injury_type}</p>
                <p><strong>Status:</strong> {injury.status}</p>
                <p><strong>Expected Return:</strong> {injury.return_date.strftime('%d %b %Y') if injury.return_date else 'TBD'}</p>
            </div>
            """, unsafe_allow_html=True)
    
    @staticmethod
    def render_recent_matches(matches: List[Match]):
        """Render recent matches panel"""
        st.markdown("---")
        st.subheader("📋 Recent Matches")
        
        for match in matches:
            # Determine match result
            if match.home_score > match.away_score:
                result = "WIN" if match.home_team != matches[0].home_team or matches[0].home_team == match.away_team else "LOSS"
            elif match.home_score < match.away_score:
                result = "LOSS" if match.home_team != matches[0].home_team else "WIN"
            else:
                result = "DRAW"
            
            result_color = "#00aa00" if result == "WIN" else "#ff0000" if result == "LOSS" else "#ffaa00"
            
            st.markdown(f"""
            <div style='background-color: #1a1a2e; padding: 15px; border-radius: 8px; 
            border-left: 4px solid {result_color}; margin-bottom: 10px;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div>
                        <p style='font-size: 12px; color: #888;'>{match.match_date.strftime('%d %b %Y')} • {match.competition}</p>
                        <p style='margin: 0;'><strong>{match.home_team}</strong> vs <strong>{match.away_team}</strong></p>
                    </div>
                    <div style='text-align: right;'>
                        <p style='font-size: 24px; font-weight: bold; margin: 0;'>{match.home_score}-{match.away_score}</p>
                        <p style='color: {result_color}; font-weight: bold; margin: 0;'>{result}</p>
                    </div>
                </div>
                <p style='font-size: 12px; color: #888; margin-top: 5px;'>📍 {match.venue}</p>
            </div>
            """, unsafe_allow_html=True)
    
    @staticmethod
    def render_insights_panel(insights: Dict[str, str]):
        """Render AI insights panel with Sky Sports style"""
        st.markdown("---")
        st.subheader("🧠 AI-Powered Insights")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div style='background-color: #1a1a2e; padding: 20px; border-radius: 8px; 
            border-left: 4px solid #004d99; margin-bottom: 15px;'>
                <h4 style='color: #004d99;'>⚔️ Attacking Play</h4>
                <p>{insights.get('finishing_efficiency', 'N/A')}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: #1a1a2e; padding: 20px; border-radius: 8px; 
            border-left: 4px solid #004d99; margin-bottom: 15px;'>
                <h4 style='color: #004d99;'>🛡️ Defense</h4>
                <p>{insights.get('defensive_performance', 'N/A')}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style='background-color: #1a1a2e; padding: 20px; border-radius: 8px; 
            border-left: 4px solid #ff6b00; margin-bottom: 15px;'>
                <h4 style='color: #ff6b00;'>🎯 Possession</h4>
                <p>{insights.get('possession_effectiveness', 'N/A')}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: #1a1a2e; padding: 20px; border-radius: 8px; 
            border-left: 4px solid #ff6b00; margin-bottom: 15px;'>
                <h4 style='color: #ff6b00;'>📊 Summary</h4>
                <p><em>{insights.get('overall_assessment', 'N/A')}</em></p>
            </div>
            """, unsafe_allow_html=True)
    
    @staticmethod
    def render_summary_panel(bullets: List[str], team_name: str):
        """Render summary panel with key insights"""
        st.markdown("---")
        st.subheader(f"📌 {team_name} - Key Takeaways")
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #004d99, #1a1a2e); padding: 25px; 
        border-radius: 8px; border: 2px solid #ff6b00;'>
            <h3 style='color: #ff6b00; margin-top: 0;'>Season Summary</h3>
        """, unsafe_allow_html=True)
        
        for bullet in bullets:
            st.markdown(f"- {bullet}")
        
        st.markdown("</div>", unsafe_allow_html=True)
