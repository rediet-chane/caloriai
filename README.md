# 🍽️ CaloriAI

Snap a photo of food. Get instant calorie and nutrition estimates.

## What it does
- 📸 Take a photo of your meal
- 🤖 AI identifies the food and estimates calories + macros
- 📊 Track daily intake with a dashboard
- 🕐 See your meal history

## Tech Stack
- **App:** Flutter
- **Backend:** Python + FastAPI
- **Database & Auth:** Supabase
- **AI:** OpenAI Vision

## Setup

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add your keys
uvicorn main:app --reload --port 8000
