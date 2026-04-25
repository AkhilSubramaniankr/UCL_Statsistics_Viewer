"""
Data management - all 7 UCL teams with proper Streamlit caching
"""
import streamlit as st
from typing import List, Optional
from datetime import date, timedelta
import os
from dotenv import load_dotenv
from .models import TeamStats, PlayerStats, InjuryReport, Match

load_dotenv()

# Fixed base date — avoids datetime.now() inside cached functions
# which caused cache misses on every rerun (was the main slowness cause)
_BASE_DATE = date(2024, 4, 1)


class DataManager:
    def __init__(self):
        self.api_key = os.getenv("FOOTBALL_API_KEY")
        self.base_url = os.getenv("FOOTBALL_API_BASE_URL", "https://api.football-data.org/v4")

    def get_team_stats(self, team_name: str) -> Optional[TeamStats]:
        return _cached_team_stats(team_name)

    def get_player_stats(self, team_name: str) -> List[PlayerStats]:
        return _cached_player_stats(team_name)

    def get_injury_reports(self, team_name: str) -> List[InjuryReport]:
        return _cached_injury_reports(team_name)

    def get_recent_matches(self, team_name: str, limit: int = 5) -> List[Match]:
        return _cached_recent_matches(team_name, limit)


@st.cache_data(ttl=1800, show_spinner=False)
def _cached_team_stats(team_name: str) -> Optional[TeamStats]:
    data = {
        "Manchester City": TeamStats("1", "Manchester City", 6, 18.0, 15.2, 4.0, 6.1, 62.3, 2),
        "Real Madrid":     TeamStats("2", "Real Madrid",     6, 16.0, 14.8, 5.0, 5.5, 58.1, 1),
        "Bayern Munich":   TeamStats("3", "Bayern Munich",   6, 19.0, 16.5, 3.0, 4.2, 65.0, 3),
        "PSG":             TeamStats("4", "PSG",             6, 14.0, 13.0, 6.0, 5.8, 56.0, 1),
        "Inter Milan":     TeamStats("5", "Inter Milan",     6, 12.0, 11.5, 5.0, 5.2, 52.0, 2),
        "Liverpool":       TeamStats("6", "Liverpool",       6, 17.0, 14.9, 5.0, 6.0, 59.0, 2),
        "Arsenal":         TeamStats("7", "Arsenal",         6, 15.0, 14.1, 4.0, 5.0, 60.0, 2),
    }
    return data.get(team_name, data["Manchester City"])


@st.cache_data(ttl=1800, show_spinner=False)
def _cached_player_stats(team_name: str) -> List[PlayerStats]:
    data = {
        "Manchester City": [
            PlayerStats("1",  "Erling Haaland",       "1", "ST",  12, 2, 8.5, 480, 45),
            PlayerStats("2",  "Bernardo Silva",        "1", "MF",   4, 3, 3.2, 540, 32),
            PlayerStats("3",  "Rodri",                 "1", "MF",   2, 1, 0.8, 540, 12),
            PlayerStats("4",  "Kyle Walker",           "1", "DEF",  0, 0, 0.1, 540,  5),
            PlayerStats("5",  "Ederson",               "1", "GK",   0, 0, 0.0, 540,  0),
        ],
        "Real Madrid": [
            PlayerStats("6",  "Jude Bellingham",       "2", "MF",  5, 1, 3.8, 480, 28),
            PlayerStats("7",  "Vinícius Júnior",       "2", "FW",  6, 2, 4.5, 510, 38),
            PlayerStats("8",  "Luka Modrić",           "2", "MF",  1, 2, 0.5, 480, 15),
            PlayerStats("9",  "Eder Militao",          "2", "DEF", 0, 0, 0.2, 540,  3),
            PlayerStats("10", "Andriy Lunin",          "2", "GK",  0, 0, 0.0, 540,  0),
        ],
        "Bayern Munich": [
            PlayerStats("11", "Harry Kane",            "3", "ST",  10, 3, 7.8, 480, 42),
            PlayerStats("12", "Leroy Sané",            "3", "FW",   5, 4, 3.5, 490, 28),
            PlayerStats("13", "Joshua Kimmich",        "3", "MF",   2, 5, 1.1, 540, 14),
            PlayerStats("14", "Alphonso Davies",       "3", "DEF",  1, 2, 0.4, 530,  8),
            PlayerStats("15", "Manuel Neuer",          "3", "GK",   0, 0, 0.0, 540,  0),
        ],
        "PSG": [
            PlayerStats("16", "Kylian Mbappé",         "4", "FW",   8, 3, 6.2, 460, 36),
            PlayerStats("17", "Ousmane Dembélé",       "4", "FW",   4, 5, 3.1, 480, 25),
            PlayerStats("18", "Vitinha",               "4", "MF",   2, 2, 1.0, 520, 18),
            PlayerStats("19", "Marquinhos",            "4", "DEF",  1, 0, 0.3, 540,  6),
            PlayerStats("20", "Gianluigi Donnarumma",  "4", "GK",   0, 0, 0.0, 540,  0),
        ],
        "Inter Milan": [
            PlayerStats("21", "Lautaro Martínez",      "5", "ST",   7, 2, 5.5, 470, 32),
            PlayerStats("22", "Marcus Thuram",         "5", "FW",   4, 3, 3.0, 490, 24),
            PlayerStats("23", "Nicolò Barella",        "5", "MF",   2, 4, 1.2, 530, 16),
            PlayerStats("24", "Alessandro Bastoni",    "5", "DEF",  1, 1, 0.4, 540,  7),
            PlayerStats("25", "Yann Sommer",           "5", "GK",   0, 0, 0.0, 540,  0),
        ],
        "Liverpool": [
            PlayerStats("26", "Mohamed Salah",         "6", "FW",   9, 4, 6.8, 470, 38),
            PlayerStats("27", "Darwin Núñez",          "6", "ST",   6, 2, 4.5, 450, 30),
            PlayerStats("28", "Dominik Szoboszlai",    "6", "MF",   3, 3, 1.8, 510, 20),
            PlayerStats("29", "Virgil van Dijk",       "6", "DEF",  1, 0, 0.5, 540,  5),
            PlayerStats("30", "Alisson Becker",        "6", "GK",   0, 0, 0.0, 540,  0),
        ],
        "Arsenal": [
            PlayerStats("31", "Bukayo Saka",           "7", "FW",   7, 5, 5.2, 480, 34),
            PlayerStats("32", "Leandro Trossard",      "7", "FW",   4, 3, 2.8, 460, 22),
            PlayerStats("33", "Martin Ødegaard",       "7", "MF",   3, 4, 2.1, 500, 19),
            PlayerStats("34", "William Saliba",        "7", "DEF",  1, 0, 0.3, 540,  4),
            PlayerStats("35", "David Raya",            "7", "GK",   0, 0, 0.0, 540,  0),
        ],
    }
    return data.get(team_name, data["Manchester City"])


@st.cache_data(ttl=1800, show_spinner=False)
def _cached_injury_reports(team_name: str) -> List[InjuryReport]:
    d = _BASE_DATE
    data = {
        "Manchester City": [
            InjuryReport("i1", "Kalvin Phillips",       "1", "Hamstring",    d + timedelta(days=14), "Out"),
            InjuryReport("i2", "Manuel Akanji",         "1", "Muscle strain",d + timedelta(days=7),  "Doubtful"),
        ],
        "Real Madrid": [
            InjuryReport("i3", "Aurélien Tchouaméni",   "2", "Ankle",        d + timedelta(days=21), "Out"),
        ],
        "Bayern Munich": [
            InjuryReport("i4", "Kingsley Coman",        "3", "Knee",         d + timedelta(days=10), "Doubtful"),
        ],
        "PSG": [
            InjuryReport("i5", "Lucas Hernández",       "4", "ACL",          d + timedelta(days=60), "Out"),
        ],
        "Inter Milan": [
            InjuryReport("i6", "Joaquín Correa",        "5", "Thigh",        d + timedelta(days=5),  "Doubtful"),
        ],
        "Liverpool": [
            InjuryReport("i7", "Diogo Jota",            "6", "Hamstring",    d + timedelta(days=14), "Out"),
        ],
        "Arsenal": [
            InjuryReport("i8", "Takehiro Tomiyasu",     "7", "Calf",         d + timedelta(days=7),  "Doubtful"),
        ],
    }
    return data.get(team_name, [])


@st.cache_data(ttl=1800, show_spinner=False)
def _cached_recent_matches(team_name: str, limit: int) -> List[Match]:
    d = _BASE_DATE
    data = {
        "Manchester City": [
            Match("m1",  "Manchester City", "PSG",              3, 0, d - timedelta(days=7),  "Champions League", "Etihad Stadium"),
            Match("m2",  "Real Madrid",     "Manchester City",  1, 0, d - timedelta(days=14), "Champions League", "Santiago Bernabéu"),
            Match("m3",  "Manchester City", "Bayern Munich",    2, 2, d - timedelta(days=21), "Champions League", "Etihad Stadium"),
            Match("m4",  "Inter Milan",     "Manchester City",  0, 1, d - timedelta(days=28), "Champions League", "San Siro"),
            Match("m5",  "Manchester City", "Napoli",           3, 1, d - timedelta(days=35), "Champions League", "Etihad Stadium"),
        ],
        "Real Madrid": [
            Match("m6",  "Real Madrid",     "Manchester City",  1, 0, d - timedelta(days=7),  "Champions League", "Santiago Bernabéu"),
            Match("m7",  "Real Madrid",     "Napoli",           4, 2, d - timedelta(days=14), "Champions League", "Santiago Bernabéu"),
            Match("m8",  "Union Berlin",    "Real Madrid",      0, 2, d - timedelta(days=21), "Champions League", "Stadion An der Alten Försterei"),
            Match("m9",  "Real Madrid",     "Braga",            3, 0, d - timedelta(days=28), "Champions League", "Santiago Bernabéu"),
            Match("m10", "Real Madrid",     "PSG",              1, 1, d - timedelta(days=35), "Champions League", "Santiago Bernabéu"),
        ],
        "Bayern Munich": [
            Match("m11", "Bayern Munich",   "Manchester City",  2, 2, d - timedelta(days=7),  "Champions League", "Allianz Arena"),
            Match("m12", "Bayern Munich",   "Galatasaray",      3, 1, d - timedelta(days=14), "Champions League", "Allianz Arena"),
            Match("m13", "Copenhagen",      "Bayern Munich",    1, 2, d - timedelta(days=21), "Champions League", "Parken Stadium"),
            Match("m14", "Bayern Munich",   "Arsenal",          2, 2, d - timedelta(days=28), "Champions League", "Allianz Arena"),
            Match("m15", "Bayern Munich",   "Lazio",            3, 0, d - timedelta(days=35), "Champions League", "Allianz Arena"),
        ],
        "PSG": [
            Match("m16", "Manchester City", "PSG",              3, 0, d - timedelta(days=7),  "Champions League", "Etihad Stadium"),
            Match("m17", "PSG",             "Borussia Dortmund",2, 0, d - timedelta(days=14), "Champions League", "Parc des Princes"),
            Match("m18", "AC Milan",        "PSG",              1, 2, d - timedelta(days=21), "Champions League", "San Siro"),
            Match("m19", "PSG",             "Real Madrid",      1, 1, d - timedelta(days=35), "Champions League", "Parc des Princes"),
            Match("m20", "PSG",             "Newcastle",        2, 1, d - timedelta(days=42), "Champions League", "Parc des Princes"),
        ],
        "Inter Milan": [
            Match("m21", "Inter Milan",     "Manchester City",  0, 1, d - timedelta(days=7),  "Champions League", "San Siro"),
            Match("m22", "Inter Milan",     "Real Sociedad",    1, 0, d - timedelta(days=14), "Champions League", "San Siro"),
            Match("m23", "Salzburg",        "Inter Milan",      0, 1, d - timedelta(days=21), "Champions League", "Red Bull Arena"),
            Match("m24", "Inter Milan",     "Benfica",          1, 0, d - timedelta(days=28), "Champions League", "San Siro"),
            Match("m25", "Inter Milan",     "Atletico Madrid",  1, 0, d - timedelta(days=35), "Champions League", "San Siro"),
        ],
        "Liverpool": [
            Match("m26", "Liverpool",       "LASK",             4, 0, d - timedelta(days=7),  "Champions League", "Anfield"),
            Match("m27", "Toulouse",        "Liverpool",        3, 2, d - timedelta(days=14), "Champions League", "Stadium de Toulouse"),
            Match("m28", "Liverpool",       "Union SG",         2, 0, d - timedelta(days=21), "Champions League", "Anfield"),
            Match("m29", "Liverpool",       "Real Madrid",      1, 0, d - timedelta(days=28), "Champions League", "Anfield"),
            Match("m30", "Bayer Leverkusen","Liverpool",        0, 1, d - timedelta(days=35), "Champions League", "BayArena"),
        ],
        "Arsenal": [
            Match("m31", "Arsenal",         "Bayern Munich",    2, 2, d - timedelta(days=7),  "Champions League", "Emirates Stadium"),
            Match("m32", "Lens",            "Arsenal",          1, 6, d - timedelta(days=14), "Champions League", "Stade Bollaert-Delelis"),
            Match("m33", "Arsenal",         "Sevilla",          2, 0, d - timedelta(days=21), "Champions League", "Emirates Stadium"),
            Match("m34", "PSV Eindhoven",   "Arsenal",          1, 4, d - timedelta(days=28), "Champions League", "Philips Stadion"),
            Match("m35", "Arsenal",         "PSV Eindhoven",    4, 0, d - timedelta(days=35), "Champions League", "Emirates Stadium"),
        ],
    }
    return data.get(team_name, data["Manchester City"])[:limit]
