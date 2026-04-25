"""
Project Configuration and Settings
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY", "")
FOOTBALL_API_BASE_URL = os.getenv("FOOTBALL_API_BASE_URL", "https://api.football-data.org/v4")

# Application Configuration
APP_TITLE = os.getenv("APP_TITLE", "UCL Elite Analytics Platform")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
CACHE_EXPIRY_MINUTES = int(os.getenv("CACHE_EXPIRY_MINUTES", "30"))

# UI Configuration
UI_THEME = "dark"
PRIMARY_COLOR = "#004d99"
SECONDARY_COLOR = "#1a1a2e"
ACCENT_COLOR = "#ff6b00"

# Teams available in demo
DEMO_TEAMS = [
    "Manchester City",
    "Real Madrid",
    "Bayern Munich",
    "PSG",
    "Inter Milan",
    "Liverpool",
    "Arsenal",
    "Barcelona"
]

# Feature flags
FEATURES = {
    "enable_ai_insights": True,
    "enable_api_integration": True,
    "enable_caching": True,
    "enable_injury_reports": True,
    "enable_match_history": True,
    "enable_player_stats": True,
}

# Cache settings
CACHE_CONFIG = {
    "max_size": 100,
    "ttl_minutes": CACHE_EXPIRY_MINUTES,
    "enabled": True
}

def is_configured():
    """Check if all required configurations are set"""
    required = ["OPENAI_API_KEY"]
    return all(os.getenv(key) for key in required)

def validate_config():
    """Validate configuration and print status"""
    print("Configuration Status:")
    print(f"  OpenAI API Key: {'✓' if OPENAI_API_KEY else '✗ Not configured'}")
    print(f"  Football API Key: {'✓' if FOOTBALL_API_KEY else '✓ Optional (demo mode)'}")
    print(f"  Debug Mode: {DEBUG_MODE}")
    print(f"  Cache Expiry: {CACHE_EXPIRY_MINUTES} minutes")
    print(f"  Features Enabled: {sum(FEATURES.values())}/{len(FEATURES)}")
