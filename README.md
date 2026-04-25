# UCL Elite Analytics Platform

A full-stack Streamlit-based football analytics platform with AI-generated insights for UEFA Champions League teams.

## Features

### ⚽ Core Features

- **Team Analytics**: Real-time team statistics including goals, xG, possession, and defensive metrics
- **Player Performance**: Track individual player stats (goals, assists, xG, minutes, shots)
- **Injury Management**: Monitor player injuries and return dates
- **Match History**: View recent matches and results
- **AI Insights**: GPT-powered tactical analysis and broadcast-style commentary
- **Sky Sports UI**: Professional dark-themed interface with smooth animations

### 📊 Data Sections

1. **Overview Dashboard**: Key metrics and performance visualizations
2. **Player Stats**: Sortable player performance table
3. **Injury Report**: Current player injuries and statuses
4. **Recent Matches**: Match history with results
5. **AI Insights**: Tactical analysis and summary bullets

## Tech Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **AI**: OpenAI GPT API
- **Data Source**: Football Data API
- **Caching**: Cachetools

## Installation

### Prerequisites

- Python 3.8 or higher
- pip or conda

### Setup Steps

1. **Clone or navigate to project directory**:
   ```bash
   cd c:\Projects\UCL
   ```

2. **Create virtual environment** (optional but recommended):
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your API keys
   ```

5. **Set up .env file** with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   FOOTBALL_API_KEY=your_football_api_key_here
   ```

## Running the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

## Project Structure

```
UCL/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment variables
├── .gitignore              # Git ignore rules
│
├── utils/                   # Utility modules
│   ├── __init__.py
│   ├── models.py           # Data models
│   ├── data_manager.py     # Data fetching & caching
│   ├── insight_generator.py # AI insight generation
│   └── ui_components.py    # Sky Sports UI components
│
├── data/                    # Data storage (mock/cached)
│
├── pages/                   # Additional Streamlit pages (future)
│
└── assets/                  # Images/resources
```

## Configuration

### Environment Variables

Create a `.env` file with:

```env
# OpenAI API
OPENAI_API_KEY=sk-...

# Football Data API
FOOTBALL_API_KEY=your_api_key
FOOTBALL_API_BASE_URL=https://api.football-data.org/v4

# Application
APP_TITLE=UCL Elite Analytics Platform
DEBUG_MODE=False
CACHE_EXPIRY_MINUTES=30
```

## API Integration

### Football Data API

The app integrates with Football Data API for real team/player data:

1. Register at https://www.football-data.org/
2. Get your API key
3. Add to `.env` file

### OpenAI GPT API

For AI-powered insights:

1. Sign up at https://platform.openai.com/
2. Create an API key
3. Add to `.env` file

## Usage

1. **Select Team**: Use the sidebar dropdown to select a Champions League team
2. **View Tabs**:
   - **Overview**: Key metrics and performance charts
   - **Players**: Top player statistics
   - **Injuries**: Current injury status
   - **Matches**: Recent match results
   - **Insights**: AI analysis and tactical summary

3. **Refresh Data**: Click "Refresh Data" button to fetch latest information

## Insight Generation

The AI insights engine analyzes:

- **Finishing Efficiency**: Goals vs Expected Goals (xG)
- **Defensive Performance**: Goals Conceded vs Expected Goals Against (xGA)
- **Possession Effectiveness**: Possession % vs Expected Goals Created
- **Overall Assessment**: Sky Sports style broadcast commentary

### Insight Rules

```
Goals > xG (1.15x) → Clinical Finishing ✓
Goals < xG (0.85x) → Poor Finishing ✗
High Possession + Low xG → Inefficient Attack
Low Conceded + High xGA → Defensive Overperformance
```

## Data Updates

- **Cache Duration**: 30 minutes (configurable)
- **Real-time**: Live API calls to Football Data API
- **Mock Data**: Included for demo purposes

## Styling

### Sky Sports Color Scheme

- **Primary**: #004d99 (Sky Blue)
- **Secondary**: #1a1a2e (Dark Gray)
- **Accent**: #ff6b00 (Orange)
- **Background**: #0f0f1e (Very Dark)

## Troubleshooting

### API Key Issues

- Ensure `.env` file is properly configured
- Check API key validity
- Verify rate limits haven't been exceeded

### Data Not Loading

- Click "Refresh Data" button
- Check internet connection
- Verify API endpoints are accessible

### UI Display Issues

- Clear browser cache
- Try in incognito/private mode
- Update Streamlit: `pip install --upgrade streamlit`

## Future Enhancements

- [ ] Real-time data integration
- [ ] Advanced predictive analytics
- [ ] Custom report generation
- [ ] Team comparison tools
- [ ] Betting odds integration
- [ ] Historical trend analysis
- [ ] Mobile app version

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review API documentation
3. Check Streamlit docs at https://docs.streamlit.io/

## License

MIT License - Feel free to use and modify for your needs

---

**Created**: 2024
**Version**: 1.0.0
**Status**: Active Development

## Deployment

You can deploy this project several ways. Two recommended options:

- Container (Docker): build the included `Dockerfile` and run locally or push to your container registry.

   ```bash
   docker build -t ucl-analytics:latest .
   docker run -p 8501:8501 ucl-analytics:latest
   ```

- Streamlit Community Cloud / Render: connect this GitHub repository to the platform and set the following environment variables in the service settings: `OPENAI_API_KEY`, `FOOTBALL_API_KEY` (optional).

For Heroku-compatible platforms using `Procfile`:

   ```bash
   heroku create my-ucl-analytics
   git push heroku main
   heroku config:set OPENAI_API_KEY=your_key_here
   heroku open
   ```

Notes:
- Make sure to copy `.env.example` to `.env` and add real API keys locally. Never commit `.env`.
- The included GitHub Actions workflow will build the Docker image on pushes to `main`. It currently does not push the image; modify `push: true` and configure secrets to enable pushing.
