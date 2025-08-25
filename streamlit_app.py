import os
import textwrap
from typing import List, Dict
import streamlit as st
import pandas as pd
import numpy as np

from pitch_modules.gemini_client import get_gemini, ensure_api_key
from pitch_modules.prompt_library import (
    prompt_investor_summary, prompt_elevator_pitch, prompt_swot, prompt_storytelling,
    prompt_risks, prompt_team_analyzer, prompt_funding_ask, prompt_competitor_table,
    prompt_pitch_email, prompt_qna
)
from pitch_modules.financials import simple_projection_table
from pitch_modules.market_size import estimate_tam_sam_som

st.set_page_config(page_title="Startup Pitch Polisher", page_icon="📑", layout="wide")

with st.sidebar:
    st.header("🔧 Configuration")
    api_key = st.text_input("Gemini API Key", value=os.environ.get("GOOGLE_API_KEY", ""), type="password")
    model_name = st.selectbox("Model", ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.0-pro"], index=0)
    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.6, 0.05)
    max_output_tokens = st.slider("Max output tokens", 256, 2048, 1024, 64)
    st.caption("Your API key is only used locally in your browser session.")

st.title("📑 Startup Pitch Polisher")
st.write("Turn raw ideas into investor-ready outputs in minutes.")

# Input area
st.subheader("1) Paste your raw idea or pitch content")
user_input = st.text_area("Raw Idea / Draft", height=220, placeholder="Paste your messy notes, bullet points, or short description here...")

# Optional extra data
with st.expander("Add Optional Context (recommended)"):
    industry = st.text_input("Industry / Domain", placeholder="Fintech, Edtech, Healthtech, etc.")
    geo = st.text_input("Target Geography", placeholder="India, US, Global, etc.")
    audience = st.text_input("Primary Customers / Users", placeholder="e.g., college students, SMEs, parents...")
    traction = st.text_area("Early Traction (metrics, users, pilots, revenue)", height=100)
    team = st.text_area("Team (founders, roles, skills)", height=100)
    competitors_raw = st.text_area("Competitors (comma separated)", placeholder="CompA, CompB, CompC")
    pricing = st.text_input("Pricing / Business Model", placeholder="Subscription, commission, freemium, etc.")
    channels = st.text_input("Go-To-Market Channels", placeholder="Campus ambassadors, SEO, partnerships...")

st.subheader("2) Select Outputs")
cols = st.columns(3)
with cols[0]:
    want_summary = st.checkbox("Investor Summary", True)
    want_elevator = st.checkbox("Elevator Pitch", True)
    want_swot = st.checkbox("SWOT Analysis", True)
    want_email = st.checkbox("Custom Pitch Email", True)
with cols[1]:
    want_financials = st.checkbox("Financial Snapshot (1-year)", True)
    want_market = st.checkbox("Market Size (TAM-SAM-SOM)", True)
    want_competitors = st.checkbox("Competitor Benchmarking", True)
    want_story = st.checkbox("Storytelling Enhancer", True)
with cols[2]:
    want_risks = st.checkbox("Risk Analysis & Mitigation", True)
    want_team = st.checkbox("Team Strength Analyzer", True)
    want_funding = st.checkbox("Funding Ask Auto-Generator", True)
    want_qna = st.checkbox("Pitch Practice Mode (Q&A)", False)

go = st.button("🚀 Generate")

if go:
    ensure_api_key(api_key)
    genai = get_gemini(api_key, model_name, temperature, max_output_tokens)
    if not user_input.strip():
        st.warning("Please enter your raw idea first.")
        st.stop()

    ctx = {
        "idea": user_input.strip(),
        "industry": industry.strip(),
        "geo": geo.strip(),
        "audience": audience.strip(),
        "traction": traction.strip(),
        "team": team.strip(),
        "pricing": pricing.strip(),
        "channels": channels.strip(),
    }

    # Outputs
    if want_summary:
        st.markdown("### 💼 Investor Summary")
        res = genai.generate_content(prompt_investor_summary(ctx))
        st.write(res.text)

    if want_elevator:
        st.markdown("### 🛗 Elevator Pitch (30s)")
        res = genai.generate_content(prompt_elevator_pitch(ctx))
        st.write(res.text)

    if want_swot:
        st.markdown("### 🧭 SWOT Analysis")
        res = genai.generate_content(prompt_swot(ctx))
        st.write(res.text)

    if want_email:
        st.markdown("### ✉️ Custom Pitch Email")
        res = genai.generate_content(prompt_pitch_email(ctx))
        st.write(res.text)

    if want_financials:
        st.markdown("### 💹 Financial Snapshot (Simple 12-month Projection)")
        pricing_hint = pricing or "subscription"
        df_fin = simple_projection_table(months=12, base_users=100, monthly_growth=0.15, arpu=5.0, cogs_pct=0.25, opex=2000.0)
        st.dataframe(df_fin, use_container_width=True)
        st.caption("Assumptions are editable in code: ARPU, growth, COGS%, fixed OPEX.")

    if want_market:
        st.markdown("### 🌍 Market Size Estimator (TAM–SAM–SOM)")
        tam, sam, som = estimate_tam_sam_som(top_down_total=1_000_000_000, serviceable_ratio=0.35, obtainable_ratio=0.07)
        st.write(f"**TAM**: ${tam:,.0f}  |  **SAM**: ${sam:,.0f}  |  **SOM**: ${som:,.0f}")
        st.caption("Adjust ratios in code or extend with real data for precision.")

    if want_competitors:
        st.markdown("### 🥊 Competitor Benchmarking")
        comp_list = [c.strip() for c in (competitors_raw or '').split(",") if c.strip()]
        if not comp_list:
            comp_list = ["Competitor A", "Competitor B", "Competitor C"]
        res = genai.generate_content(prompt_competitor_table(ctx, comp_list))
        st.write(res.text)

    if want_story:
        st.markdown("### 📖 Storytelling Enhancer (hooks & analogies)")
        res = genai.generate_content(prompt_storytelling(ctx))
        st.write(res.text)

    if want_risks:
        st.markdown("### ⚠️ Risk Analysis & Mitigation")
        res = genai.generate_content(prompt_risks(ctx))
        st.write(res.text)

    if want_team:
        st.markdown("### 👥 Team Strength Analyzer")
        res = genai.generate_content(prompt_team_analyzer(ctx))
        st.write(res.text)

    if want_funding:
        st.markdown("### 💰 Funding Ask Auto-Generator")
        res = genai.generate_content(prompt_funding_ask(ctx))
        st.write(res.text)

    if want_qna:
        st.markdown("### 🎤 Pitch Practice Mode (Q&A)")
        res = genai.generate_content(prompt_qna(ctx))
        st.write(res.text)

st.markdown("---")
st.caption("Built with Streamlit + Gemini · Extend prompts and models as needed.")
