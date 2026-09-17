# 🍽️ CaloriAI

Snap a photo of food. Get instant calorie and nutrition estimates.

## What it does
- 📸 Take a photo of your meal
- 🤖 AI identifies the food and estimates calories + macros
- 📊 Track daily intake with a dashboard
- 🕐 See your meal history
## ScreenShoots
[<img width="239" height="536" alt="image" src="https://github.com/user-attachments/assets/f74dde7c-4416-4e25-8f68-8744d707acae" />
<img width="236" height="538" alt="image" src="https://github.com/user-attachments/assets/54d2dbb0-0289-4ec3-92db-c78ed735d58e" />
<img width="242" height="536" alt="image" src="https://github.com/user-attachments/assets/44efd486-39bf-4068-a5d9-4eb59412d5b1" />
<img width="238" height="536" alt="image" src="https://github.com/user-attachments/assets/1c3ac005-bbec-4157-8be8-61a0e5807e24" />


]
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
cp .env.example .env  
uvicorn main:app --reload --port 8000
