# Project Files & Architecture Documentation

## 📋 Complete File Listing & Descriptions

### Root Level Files

#### 🚀 Core Application
- **app.py** - Main Streamlit application. Entry point for the platform.
  - Tab-based interface (Overview, Players, Injuries, Matches, Insights)
  - Team selector dropdown
  - Refresh data button
  - Integrates all modules

#### 📖 Documentation
- **README.md** - Comprehensive documentation with features, setup, configuration, troubleshooting
- **QUICKSTART.md** - Quick start guide (5-minute setup)
- **ARCHITECTURE.md** - This file - technical architecture and component descriptions

#### ⚙️ Configuration
- **config.py** - Central configuration module
  - API keys management
  - Feature flags
  - Cache settings
  - Available teams list
  - Configuration validation

- **.env.example** - Template for environment variables
  - API keys (OpenAI, Football Data)
  - App settings
  - Cache configuration

- **.env** - Actual environment variables (not in git)
  - User-specific API keys
  - Local configuration

#### 📦 Dependencies
- **requirements.txt** - Python package dependencies
  - streamlit
  - pandas, numpy
  - plotly
  - openai, requests
  - python-dotenv
  - cachetools

#### 📁 Git Configuration
- **.gitignore** - Files to ignore in version control
  - .env files
  - __pycache__
  - venv
  - IDE files

#### 🔧 Setup Scripts
- **setup.ps1** - Windows PowerShell setup script
  - Creates virtual environment
  - Installs dependencies
  - Sets up .env file

- **setup.sh** - Linux/macOS bash setup script
  - Creates virtual environment
  - Installs dependencies
  - Sets up .env file

#### 📝 Testing & Examples
- **example.py** - Example usage of the platform
  - Shows how to use DataManager
  - Shows how to use InsightGenerator

- **test_dev.py** - Development test suite
  - Tests DataManager
  - Tests InsightGenerator
  - Generates mock data

---

### 📂 utils/ Directory - Core Modules

#### 🔧 Utility Modules

**models.py** - Data models/classes
- `TeamStats`: Team statistics (goals, xG, possession, etc.)
- `PlayerStats`: Player statistics (goals, assists, xG, minutes, shots)
- `InjuryReport`: Injury information (player, injury type, return date)
- `Match`: Match information (teams, score, date, venue)

**data_manager.py** - Data fetching and caching
- `DataManager` class:
  - `get_team_stats()` - Fetch team statistics
  - `get_player_stats()` - Fetch player statistics
  - `get_injury_reports()` - Fetch injury data
  - `get_recent_matches()` - Fetch match history
  - TTL cache for performance (30 minutes default)
  - Mock data generators for demo mode
  - (Can be extended with real API calls)

**insight_generator.py** - AI insights using GPT
- `InsightGenerator` class:
  - `generate_team_insights()` - Generate tactical insights
  - `_analyze_finishing()` - Analyze finishing efficiency
  - `_analyze_defense()` - Analyze defensive performance
  - `_analyze_possession()` - Analyze possession effectiveness
  - `_generate_broadcast_summary()` - GPT-powered broadcast commentary
  - `generate_summary_bullets()` - Generate 3-5 key insights
  - Falls back to default summaries if API unavailable

**ui_components.py** - Sky Sports themed UI
- `UIComponents` class (all static methods):
  - `setup_page_config()` - Configure Streamlit theme
  - `render_key_metrics_card()` - Display 6 key metrics
  - `render_team_overview()` - Team stats visualizations
  - `render_player_stats_panel()` - Player statistics table
  - `render_injury_report()` - Injury status display
  - `render_recent_matches()` - Match history cards
  - `render_insights_panel()` - AI insights display
  - `render_summary_panel()` - Key takeaways
  - Sky Sports color scheme (blue/orange/dark)
  - Custom CSS for professional styling

**__init__.py** - Package initialization
- Exports all public classes and functions
- Makes utils a proper Python package

---

### 📂 .streamlit/ Directory

**config.toml** - Streamlit configuration
- Theme settings (Sky Sports colors)
- Logger configuration
- Server settings
- CORS and security settings

---

### 📂 data/ Directory
- Placeholder for cached/stored data
- Can be used for CSV exports
- Data persistence

---

### 📂 pages/ Directory
- Placeholder for additional Streamlit pages
- Multi-page app support
- Future analytics pages

---

### 📂 assets/ Directory
- Placeholder for images/logos
- Future branding assets

---

## 🏗️ Architecture Overview

### Data Flow

```
┌─────────────────────────────────────────┐
│          Streamlit UI (app.py)          │
│  ├─ Sidebar (Team Selection)            │
│  ├─ 5 Tab Sections                      │
│  └─ Real-time Refresh Button            │
└────────────┬────────────────────────────┘
             │
      ┌──────┴──────┐
      │             │
┌─────▼─────────┐  │  ┌──────────────────┐
│ DataManager   │──┼──│ InsightGenerator │
│               │  │  │                  │
│ ├─Team Stats  │  │  │ ├─ Finishing     │
│ ├─Players     │  │  │ ├─ Defense       │
│ ├─Injuries    │  │  │ ├─ Possession    │
│ └─Matches     │  │  │ └─ Broadcast     │
└────────┬──────┘  │  └────────┬─────────┘
         │         │           │
    ┌────▼─────┐   │       ┌───▼────┐
    │ Models   │   │       │ OpenAI │
    │ Classes  │   │       │  API   │
    └──────────┘   │       └────────┘
                   │
             ┌─────▼─────────┐
             │ UIComponents  │
             │ (Sky Sports)  │
             └───────────────┘

┌─────────────────────────────────────────┐
│           Cache Layer (TTL)             │
│  Stores: Team Stats, Players, Injuries, │
│  Matches for 30 minutes                 │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│    External APIs (Optional)             │
│  ├─ Football Data API (real data)       │
│  └─ OpenAI API (AI insights)            │
└─────────────────────────────────────────┘
```

---

## 🔄 Component Interactions

### 1. Data Retrieval Flow
```
app.py
  └─ DataManager.get_team_stats()
       └─ Check cache
            ├─ Hit: Return cached data
            └─ Miss: _mock_team_stats() → Store in cache
```

### 2. Insight Generation Flow
```
app.py
  └─ InsightGenerator.generate_team_insights()
       ├─ _analyze_finishing()
       ├─ _analyze_defense()
       ├─ _analyze_possession()
       └─ _generate_broadcast_summary()
            └─ (OpenAI API if configured, else default)
```

### 3. UI Rendering Flow
```
app.py
  ├─ Tab 1: Overview
  │   └─ UIComponents.render_key_metrics_card()
  │   └─ UIComponents.render_team_overview()
  │
  ├─ Tab 2: Players
  │   └─ UIComponents.render_player_stats_panel()
  │
  ├─ Tab 3: Injuries
  │   └─ UIComponents.render_injury_report()
  │
  ├─ Tab 4: Matches
  │   └─ UIComponents.render_recent_matches()
  │
  └─ Tab 5: Insights
      ├─ UIComponents.render_insights_panel()
      └─ UIComponents.render_summary_panel()
```

---

## 📊 Data Structure

### TeamStats
```python
team_id: str
team_name: str
matches: int
goals: float
expected_goals: float
goals_conceded: float
expected_goals_conceded: float
possession: float
clean_sheets: int
```

### PlayerStats
```python
player_id: str
player_name: str
team_id: str
position: str
goals: int
assists: int
expected_goals: float
minutes_played: int
shots: int
```

### InjuryReport
```python
player_id: str
player_name: str
team_id: str
injury_type: str
return_date: datetime
status: str  # "Out", "Doubtful", "Available"
```

### Match
```python
match_id: str
home_team: str
away_team: str
home_score: int
away_score: int
match_date: datetime
competition: str
venue: str
```

---

## 🎨 UI Component Map

### Page Layout
```
┌─────────────────────────────────────────┐
│           Header Section                │
│    "UCL ELITE ANALYTICS"                │
│    Championships League Platform        │
└─────────────────────────────────────────┘

┌──────────────┐ ┌──────────────────────┐
│              │ │                      │
│   SIDEBAR    │ │   MAIN CONTENT       │
│              │ │                      │
│ Team Select  │ │ 5 TABS:              │
│ Refresh Btn  │ │ ├─ Overview          │
│ Info Panel   │ │ ├─ Players           │
│              │ │ ├─ Injuries          │
│              │ │ ├─ Matches           │
│              │ │ └─ Insights          │
│              │ │                      │
└──────────────┘ └──────────────────────┘

┌─────────────────────────────────────────┐
│           Footer Section                │
│    Copyright & Links                    │
└─────────────────────────────────────────┘
```

---

## 🔌 Extension Points

### Add Real Data Integration
```python
# In data_manager.py, replace mock methods with:
def _mock_team_stats(self, team_name: str) -> TeamStats:
    response = requests.get(
        f"{self.base_url}/teams",
        headers={"X-Auth-Token": self.api_key}
    )
    # Parse and return real data
```

### Add Custom Insights
```python
# In insight_generator.py, add new analysis:
def _analyze_custom(self, stats: TeamStats) -> str:
    # Your custom analysis logic
    return "Insight text"
```

### Add New Visualizations
```python
# In ui_components.py, add new methods:
@staticmethod
def render_custom_chart(data):
    fig = go.Figure(...)
    st.plotly_chart(fig)
```

### Add New UI Pages
```
# Create pages/01_advanced_stats.py
# Streamlit will auto-add to navigation
```

---

## 🔐 Security Considerations

- API keys stored in .env (never committed)
- .gitignore prevents accidental commits
- Cache TTL prevents stale data
- Input validation on team selector
- No direct database access (API only)

---

## ⚡ Performance Optimization

- **Caching**: TTL cache for 30 minutes (configurable)
- **Lazy Loading**: Data fetched on demand
- **Streamlit Caching**: @st.cache_data decorator (add as needed)
- **Efficient Rendering**: Only render visible tabs
- **Batch API Calls**: Multiple stats fetched together

---

## 🚀 Deployment Checklist

- [ ] Test all features locally
- [ ] Configure production API keys
- [ ] Test with real data API (optional)
- [ ] Update .env for production
- [ ] Set DEBUG_MODE=False
- [ ] Review error handling
- [ ] Test on target platform
- [ ] Monitor performance
- [ ] Set up logging

---

This architecture provides a scalable, maintainable foundation for the UCL Elite Analytics Platform with clear separation of concerns and extensibility for future features.
