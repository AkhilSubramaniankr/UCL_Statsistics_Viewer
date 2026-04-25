"""
AI-powered insights generation using GPT
"""
import os
from typing import Dict, List
from dotenv import load_dotenv
from .models import TeamStats, PlayerStats

load_dotenv()

class InsightGenerator:
    """Generates AI-powered insights using OpenAI GPT"""
    
    def __init__(self):
        try:
            import openai
            self.openai = openai
            self.api_key = os.getenv("OPENAI_API_KEY")
            if self.api_key:
                openai.api_key = self.api_key
        except ImportError:
            self.openai = None
    
    def generate_team_insights(self, team_stats: TeamStats) -> Dict[str, str]:
        """Generate tactical insights for a team"""
        
        # Calculate performance metrics
        insights = {
            "finishing_efficiency": self._analyze_finishing(team_stats),
            "defensive_performance": self._analyze_defense(team_stats),
            "possession_effectiveness": self._analyze_possession(team_stats),
            "overall_assessment": self._generate_broadcast_summary(team_stats)
        }
        
        return insights
    
    def _analyze_finishing(self, stats: TeamStats) -> str:
        """Analyze finishing efficiency"""
        if stats.goals > stats.expected_goals * 1.15:
            return "🎯 **Clinical Finishing** - The team is significantly outperforming expected goals, demonstrating excellent conversion efficiency."
        elif stats.goals < stats.expected_goals * 0.85:
            return "❌ **Poor Finishing** - Underperforming expected goals indicates missed opportunities and conversion issues."
        else:
            return "✓ **Balanced Finishing** - Goals align with expected xG. Consistent performance in front of goal."
    
    def _analyze_defense(self, stats: TeamStats) -> str:
        """Analyze defensive performance"""
        if stats.goals_conceded < stats.expected_goals_conceded * 0.85:
            return "🛡️ **Defensive Mastery** - Conceding fewer goals than expected. Excellent defensive organization and goalkeeper performance."
        elif stats.goals_conceded > stats.expected_goals_conceded * 1.15:
            return "⚠️ **Defensive Vulnerability** - Conceding more goals than expected xGA. Defensive solidity needs improvement."
        else:
            return "✓ **Solid Defense** - Goals conceded align with expected metrics. Reliable defensive performance."
    
    def _analyze_possession(self, stats: TeamStats) -> str:
        """Analyze possession and attacking effectiveness"""
        if stats.possession > 55 and stats.expected_goals > 1.5:
            return "⚡ **Dominant Play** - High possession combined with strong attacking metrics. Team controls the game."
        elif stats.possession > 55 and stats.expected_goals < 1.2:
            return "📊 **Possession Inefficiency** - High possession but low xG. Lacking penetration and clear-cut chances."
        else:
            return "⚙️ **Balanced Approach** - Moderate possession with efficient chance creation."
    
    def _generate_broadcast_summary(self, stats: TeamStats) -> str:
        """Generate Sky Sports style broadcast summary"""
        prompt = f"""
        You are a Sky Sports commentator. Generate a brief, exciting tactical summary (2-3 sentences) 
        for {stats.team_name} based on these stats:
        - Goals: {stats.goals} (xG: {stats.expected_goals})
        - Goals Conceded: {stats.goals_conceded} (xGA: {stats.expected_goals_conceded})
        - Possession: {stats.possession}%
        - Matches: {stats.matches}
        - Clean Sheets: {stats.clean_sheets}
        
        Style: Energetic, professional, match commentary style.
        """
        
        if self.openai and self.api_key:
            try:
                response = self.openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=100,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                print(f"Error calling OpenAI API: {e}")
                return self._default_summary(stats)
        else:
            return self._default_summary(stats)
    
    def _default_summary(self, stats: TeamStats) -> str:
        """Default summary when API is not available"""
        performance = "impressive" if stats.goals > stats.expected_goals else "concerning"
        return f"{stats.team_name} shows {performance} performance with {stats.goals} goals " \
               f"and strong defensive organization. Possession-based approach at {stats.possession}%."
    
    def generate_summary_bullets(self, team_stats: TeamStats) -> List[str]:
        """Generate 3-5 key insight bullets"""
        bullets = []
        
        # Finishing insight
        if team_stats.goals > team_stats.expected_goals * 1.15:
            bullets.append(f"📈 Clinical finishing with {team_stats.goals} goals vs {team_stats.expected_goals:.1f} xG")
        
        # Defensive insight
        if team_stats.clean_sheets >= 2:
            bullets.append(f"🛡️ Strong defense: {team_stats.clean_sheets} clean sheets from {team_stats.matches} matches")
        
        # Possession insight
        if team_stats.possession > 60 and team_stats.expected_goals > 1.5:
            bullets.append(f"⚡ Dominant possession ({team_stats.possession}%) translating to chances")
        elif team_stats.possession > 55:
            bullets.append(f"📊 High possession but needs more cutting edge in final third")
        
        # Overall performance
        if team_stats.goals > 2.5 and team_stats.goals_conceded < 1.5:
            bullets.append("🎯 Balanced strong attacking and defensive performance")
        
        return bullets[:5]
