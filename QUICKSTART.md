# UCL Elite Analytics Platform - Quick Start Guide

## 🚀 Project Built Successfully!

Your complete UCL Elite Analytics Platform is ready to use. Follow this guide to get it running.

---

## 📋 Project Structure

```
UCL/
├── app.py                      # Main Streamlit application ⭐ START HERE
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── README.md                   # Full documentation
├── example.py                  # Example usage
├── test_dev.py                # Development tests
├── .env.example               # Environment template
├── .gitignore                 # Git configuration
│
├── utils/                     # Core modules
│   ├── __init__.py
│   ├── models.py             # Data structures (TeamStats, PlayerStats, etc.)
│   ├── data_manager.py       # API & data fetching with caching
│   ├── insight_generator.py  # AI-powered insights (GPT)
│   └── ui_components.py      # Sky Sports styled UI components
│
├── .streamlit/               # Streamlit config
│   └── config.toml          # UI theme configuration
│
├── setup.ps1                # Windows setup script
├── setup.sh                 # Linux/macOS setup script
└── data/, pages/, assets/   # Placeholder directories
```

---

## ⚡ Quick Start (5 minutes)

### Option A: Windows PowerShell

```powershell
cd c:\Projects\UCL
.\setup.ps1
streamlit run app.py
```

### Option B: macOS/Linux Terminal

```bash
cd ~/Projects/UCL
chmod +x setup.sh
./setup.sh
streamlit run app.py
```

### Option C: Manual Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API keys
# Copy and edit:
cp .env.example .env
# Edit .env with your API keys (see below)

# 5. Run the app
streamlit run app.py
```

---

## 🔑 API Configuration

### Step 1: Set Up Your API Keys

The app requires an OpenAI API key for AI insights. Optionally add a Football Data API key for real data.

#### Get OpenAI API Key:
1. Visit https://platform.openai.com/api-keys
2. Create a new API key
3. Copy it

#### Get Football Data API Key (Optional):
1. Visit https://www.football-data.org/
2. Register and create an API key
3. Copy it

### Step 2: Configure .env File

Edit `.env` in your project folder:

```env
# Required - for AI insights
OPENAI_API_KEY=sk-your-openai-key-here

# Optional - for real team data
FOOTBALL_API_KEY=your-football-api-key-here
FOOTBALL_API_BASE_URL=https://api.football-data.org/v4

# Application settings
APP_TITLE=UCL Elite Analytics Platform
DEBUG_MODE=False
CACHE_EXPIRY_MINUTES=30
```

---

## 🎮 Using the Application

### 1. Start the App

```bash
streamlit run app.py
```

The app opens at: **http://localhost:8501**

### 2. Main Features

- **📊 Overview Tab**: Key metrics, possession, goals vs xG
- **👥 Players Tab**: Top players, goals, assists, shots
- **🏥 Injuries Tab**: Player injury status and return dates
- **📋 Matches Tab**: Recent match results and stats
- **🧠 Insights Tab**: AI-powered tactical analysis

### 3. Team Selection

Use the **Team Selector** in the sidebar to choose from:
- Manchester City
- Real Madrid
- Bayern Munich
- PSG
- Inter Milan
- Liverpool
- Arsenal
- Barcelona

### 4. Data Refresh

Click **🔄 Refresh Data** to fetch the latest information (currently uses demo data).

---

## 📊 Features Overview

### ✅ Implemented Features

1. **Team Statistics**
   - Goals and Expected Goals (xG)
   - Goals Conceded and xGA
   - Possession %
   - Clean Sheets

2. **Player Performance**
   - Goals and Assists
   - Expected Goals (xG)
   - Minutes Played
   - Shot Count

3. **Injury Management**
   - Player injury type
   - Injury status (Out/Doubtful/Available)
   - Expected return date

4. **Recent Matches**
   - Match results
   - Opponent and venue
   - Match date and competition

5. **AI Insights** (GPT-Powered)
   - Finishing efficiency analysis
   - Defensive performance assessment
   - Possession effectiveness
   - Sky Sports style broadcast summary

6. **Sky Sports UI**
   - Dark theme (black/blue/orange)
   - Card-based layout
   - Smooth animations
   - Professional styling

---

## 🧪 Testing & Development

### Run Demo Tests

```bash
python test_dev.py
```

This tests:
- Data Manager functionality
- Insight generation
- Mock data loading

### Run Example

```bash
python example.py
```

Shows basic API usage examples.

---

## 🔧 Customization

### Add New Teams

Edit `config.py`:

```python
DEMO_TEAMS = [
    "Your Team Name",
    # ... more teams
]
```

### Modify AI Prompts

Edit `utils/insight_generator.py`:

```python
def _generate_broadcast_summary(self, stats: TeamStats) -> str:
    prompt = """Your custom prompt here"""
    # ...
```

### Change UI Colors

Edit `utils/ui_components.py`:

```python
PRIMARY_COLOR = "#yourcolor"
SECONDARY_COLOR = "#yourcolor"
ACCENT_COLOR = "#yourcolor"
```

---

## 🐛 Troubleshooting

### Problem: "Module not found" errors

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Problem: API key errors

**Solution:**
- Verify `.env` file exists and is in the project root
- Check API key is correct and active
- Ensure no extra spaces around the key

### Problem: Port 8501 already in use

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Problem: Slow data loading

**Solution:**
- Increase cache TTL in `.env`
- Check internet connection
- Verify API rate limits

---

## 📚 Documentation Files

- **README.md** - Full feature documentation
- **This file** - Quick start guide
- **.env.example** - Environment variable template
- **app.py** - Inline code comments
- **utils/** - Module documentation in docstrings

---

## 🎯 Next Steps

1. ✅ Install dependencies
2. ✅ Configure API keys in `.env`
3. ✅ Run `streamlit run app.py`
4. ✅ Select a team and explore
5. 📈 (Optional) Connect real Football Data API
6. 🚀 (Optional) Deploy to Streamlit Cloud

---

## 🌐 Deployment Options

### Streamlit Cloud (Free)

1. Push code to GitHub
2. Visit https://share.streamlit.io
3. Connect your GitHub repo
4. Deploy in minutes!

### Other Options

- Heroku
- AWS
- Google Cloud
- Azure
- Docker

---

## 📝 Key Technologies

- **Streamlit**: Web UI framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive charts
- **OpenAI GPT**: AI insights
- **Football Data API**: Live data
- **Python 3.8+**: Runtime

---

## ✨ Features at a Glance

| Feature | Status | API Required |
|---------|--------|-------------|
| Team Stats | ✅ Complete | Optional |
| Player Stats | ✅ Complete | Optional |
| Injury Reports | ✅ Complete | No |
| Match History | ✅ Complete | Optional |
| AI Insights | ✅ Complete | OpenAI |
| Sky Sports UI | ✅ Complete | No |
| Caching | ✅ Complete | No |
| Real-time Updates | ✅ Complete | Optional |

---

## 🎓 Learning Resources

- Streamlit Docs: https://docs.streamlit.io
- OpenAI API: https://platform.openai.com/docs
- Football Data API: https://www.football-data.org/client/register
- Python: https://www.python.org/

---

## 💡 Tips & Best Practices

1. **Cache Effectively**: Data is cached for 30 minutes by default
2. **API Keys**: Never commit .env to git (it's in .gitignore)
3. **Performance**: Use demo mode for testing without API calls
4. **Debugging**: Enable DEBUG_MODE in .env for verbose logging
5. **Updates**: Run `pip install --upgrade streamlit` periodically

---

## 🎉 You're All Set!

Your UCL Elite Analytics Platform is ready to use. Start with:

```bash
streamlit run app.py
```

Enjoy exploring Champions League analytics! ⚽

---

**Questions or Issues?**
- Check the README.md
- Review code comments in app.py
- Check Streamlit documentation
- Verify API keys are configured correctly

**Happy analyzing!** 🚀
