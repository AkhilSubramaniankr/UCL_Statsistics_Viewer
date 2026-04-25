#!/bin/bash
# UCL Elite Analytics Platform - Setup Script for macOS/Linux

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}===============================================${NC}"
echo -e "${GREEN}   UCL Elite Analytics Platform Setup${NC}"
echo -e "${YELLOW}===============================================${NC}"

# Check if Python is installed
echo -e "\n${YELLOW}[1/5]${NC} Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python not found. Please install Python 3.8 or higher.${NC}"
    exit 1
fi

# Create virtual environment
echo -e "\n${YELLOW}[2/5]${NC} Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${YELLOW}⚠ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "\n${YELLOW}[3/5]${NC} Activating virtual environment..."
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"

# Install dependencies
echo -e "\n${YELLOW}[4/5]${NC} Installing dependencies..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Dependencies installed successfully${NC}"
else
    echo -e "${RED}✗ Failed to install dependencies${NC}"
    exit 1
fi

# Setup environment file
echo -e "\n${YELLOW}[5/5]${NC} Setting up configuration..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo -e "${GREEN}✓ .env file created${NC}"
    echo -e "${YELLOW}⚠ Please edit .env and add your API keys!${NC}"
else
    echo -e "${YELLOW}⚠ .env already exists${NC}"
fi

echo -e "\n${GREEN}===============================================${NC}"
echo -e "${GREEN}   Setup Complete!${NC}"
echo -e "${GREEN}===============================================${NC}"
echo -e "\nTo start the application, run:"
echo -e "${YELLOW}   streamlit run app.py${NC}"
echo -e "\nFor more information, see README.md"
