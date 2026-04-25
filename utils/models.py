"""
Data models for football analytics
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class TeamStats:
    """Team statistics"""
    team_id: str
    team_name: str
    matches: int
    goals: float
    expected_goals: float
    goals_conceded: float
    expected_goals_conceded: float
    possession: float
    clean_sheets: int
    
@dataclass
class PlayerStats:
    """Player statistics"""
    player_id: str
    player_name: str
    team_id: str
    position: str
    goals: int
    assists: int
    expected_goals: float
    minutes_played: int
    shots: int
    
@dataclass
class InjuryReport:
    """Player injury information"""
    player_id: str
    player_name: str
    team_id: str
    injury_type: str
    return_date: Optional[datetime]
    status: str  # "Out", "Doubtful", "Available"
    
@dataclass
class Match:
    """Match information"""
    match_id: str
    home_team: str
    away_team: str
    home_score: int
    away_score: int
    match_date: datetime
    competition: str  # "Champions League", etc.
    venue: str
