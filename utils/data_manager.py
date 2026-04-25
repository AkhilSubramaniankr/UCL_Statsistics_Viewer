"""
Data management and API integration
"""
import pandas as pd
import requests
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import cachetools
from .models import TeamStats, PlayerStats, InjuryReport, Match

load_dotenv()

class DataManager:
    """Manages data fetching and caching"""
    
    def __init__(self):
        self.api_key = os.getenv("FOOTBALL_API_KEY")
        self.base_url = os.getenv("FOOTBALL_API_BASE_URL", "https://api.football-data.org/v4")
        self.cache = cachetools.TTLCache(maxsize=100, ttl=30*60)  # 30 min cache
        
    def get_team_stats(self, team_name: str) -> Optional[TeamStats]:
        """Fetch team statistics"""
        cache_key = f"team_stats_{team_name}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Mock data - replace with real API calls
        stats = self._mock_team_stats(team_name)
        self.cache[cache_key] = stats
        return stats
    
    def get_player_stats(self, team_name: str) -> List[PlayerStats]:
        """Fetch player statistics for a team"""
        cache_key = f"player_stats_{team_name}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Mock data - replace with real API calls
        stats = self._mock_player_stats(team_name)
        self.cache[cache_key] = stats
        return stats
    
    def get_injury_reports(self, team_name: str) -> List[InjuryReport]:
        """Fetch injury reports for a team"""
        cache_key = f"injury_reports_{team_name}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Mock data - replace with real API calls
        reports = self._mock_injury_reports(team_name)
        self.cache[cache_key] = reports
        return reports
    
    def get_recent_matches(self, team_name: str, limit: int = 5) -> List[Match]:
        """Fetch recent matches for a team"""
        cache_key = f"recent_matches_{team_name}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Mock data - replace with real API calls
        matches = self._mock_recent_matches(team_name, limit)
        self.cache[cache_key] = matches
        return matches
    
    # Mock data methods - replace with real API calls
    
    def _mock_team_stats(self, team_name: str) -> TeamStats:
        """Generate mock team statistics"""
        mock_data = {
            "Manchester City": TeamStats(
                team_id="1",
                team_name="Manchester City",
                matches=6,
                goals=18.0,
                expected_goals=15.2,
                goals_conceded=4.0,
                expected_goals_conceded=6.1,
                possession=62.3,
                clean_sheets=2
            ),
            "Real Madrid": TeamStats(
                team_id="2",
                team_name="Real Madrid",
                matches=6,
                goals=16.0,
                expected_goals=14.8,
                goals_conceded=5.0,
                expected_goals_conceded=5.5,
                possession=58.1,
                clean_sheets=1
            ),
            "Bayern Munich": TeamStats(
                team_id="3",
                team_name="Bayern Munich",
                matches=6,
                goals=19.0,
                expected_goals=16.5,
                goals_conceded=3.0,
                expected_goals_conceded=4.2,
                possession=65.0,
                clean_sheets=3
            ),
        }
        return mock_data.get(team_name, mock_data["Manchester City"])
    
    def _mock_player_stats(self, team_name: str) -> List[PlayerStats]:
        """Generate mock player statistics"""
        mock_players = {
            "Manchester City": [
                PlayerStats("1", "Erling Haaland", "1", "ST", 12, 2, 8.5, 480, 45),
                PlayerStats("2", "Bernardo Silva", "1", "MF", 4, 3, 3.2, 540, 32),
                PlayerStats("3", "Rodri", "1", "MF", 2, 1, 0.8, 540, 12),
                PlayerStats("4", "Kyle Walker", "1", "DEF", 0, 0, 0.1, 540, 5),
                PlayerStats("5", "Ederson", "1", "GK", 0, 0, 0.0, 540, 0),
            ],
            "Real Madrid": [
                PlayerStats("6", "Jude Bellingham", "2", "MF", 5, 1, 3.8, 480, 28),
                PlayerStats("7", "Vinícius Júnior", "2", "FW", 6, 2, 4.5, 510, 38),
                PlayerStats("8", "Luka Modrić", "2", "MF", 1, 2, 0.5, 480, 15),
                PlayerStats("9", "Eder Militao", "2", "DEF", 0, 0, 0.2, 540, 3),
                PlayerStats("10", "Andriy Lunin", "2", "GK", 0, 0, 0.0, 540, 0),
            ],
        }
        return mock_players.get(team_name, mock_players["Manchester City"])
    
    def _mock_injury_reports(self, team_name: str) -> List[InjuryReport]:
        """Generate mock injury reports"""
        mock_injuries = {
            "Manchester City": [
                InjuryReport("11", "Kalvin Phillips", "1", "Hamstring", 
                           datetime.now() + timedelta(days=14), "Out"),
                InjuryReport("12", "Manuel Akanji", "1", "Muscle strain", 
                           datetime.now() + timedelta(days=7), "Doubtful"),
            ],
            "Real Madrid": [
                InjuryReport("13", "Aurélien Tchouaméni", "2", "Ankle", 
                           datetime.now() + timedelta(days=21), "Out"),
            ],
        }
        return mock_injuries.get(team_name, [])
    
    def _mock_recent_matches(self, team_name: str, limit: int = 5) -> List[Match]:
        """Generate mock recent matches"""
        mock_matches = {
            "Manchester City": [
                Match("m1", "Manchester City", "PSG", 3, 0, 
                     datetime.now() - timedelta(days=7), "Champions League", "Etihad Stadium"),
                Match("m2", "Real Madrid", "Manchester City", 1, 0, 
                     datetime.now() - timedelta(days=14), "Champions League", "Santiago Bernabéu"),
                Match("m3", "Manchester City", "Bayern Munich", 2, 2, 
                     datetime.now() - timedelta(days=21), "Champions League", "Etihad Stadium"),
                Match("m4", "Inter Milan", "Manchester City", 0, 1, 
                     datetime.now() - timedelta(days=28), "Champions League", "San Siro"),
                Match("m5", "Manchester City", "Napoli", 3, 1, 
                     datetime.now() - timedelta(days=35), "Champions League", "Etihad Stadium"),
            ],
        }
        matches = mock_matches.get(team_name, mock_matches["Manchester City"])
        return matches[:limit]
