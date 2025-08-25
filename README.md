# Startup Pitch Polisher (Streamlit + Gemini)

An AI-powered assistant that turns raw startup ideas or messy pitch decks into investor-ready outputs.

## ✨ Features (MVP)
- Investor summary
- Elevator pitch (30s)
- SWOT analysis
- Custom pitch email
- Funding ask auto-generator
- Risk analysis & mitigation
- Team strength analyzer
- Storytelling hooks
- Market size (TAM–SAM–SOM) estimator (simple model)
- Financial snapshot (1-year revenue/cost/profit)
- Pitch practice mode (Q&A simulation)

## 🧰 Tech Stack
- Python 3.10+
- Streamlit
- google-generativeai (Gemini)
- Pandas, NumPy

## 🔑 Setup
1) Create a virtual environment and install dependencies:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

2) Set your **Gemini API key** (recommended: environment variable):
```bash
# Windows PowerShell
$Env:GEMINI_API_KEY = "YOUR_KEY_HERE"
# macOS/Linux
export GEMINI_API_KEY="YOUR_KEY_HERE"
```

Alternatively, you can add it at runtime via the app's sidebar input.


## ▶️ Run
```bash
streamlit run streamlit_app.py
```

## 📦 Project Structure
```
startup-pitch-polisher/
├── streamlit_app.py
├── requirements.txt
├── README.md
└── pitch_modules/
    ├── gemini_client.py
    ├── prompt_library.py
    ├── financials.py
    ├── market_size.py
    ├── pitch_email.py
    └── qna_simulator.py
```

## 🔌 Notes
- Competitor benchmarking uses structured user input in the MVP; you can integrate a web-scraping API later.
- Google Slides/Canva export hooks are stubbed for future scope.
- This is designed as a clean foundation—extend prompts, UI, and data models as you grow.
