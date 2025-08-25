import os
import google.generativeai as genai

def ensure_api_key(api_key: str | None = None):
    # Prefer environment variable if sidebar input is empty
    if not api_key:
        api_key = os.environ.get("GOOGLE_API_KEY", "")
    if not api_key.strip():
        raise RuntimeError("Gemini API key missing. Set GEMINI_API_KEY env var or enter in sidebar.")

    genai.configure(api_key=api_key)
    return api_key

def get_gemini(api_key: str = None, model_name: str = "gemini-1.5-flash",
               temperature: float = 0.6, max_output_tokens: int = 1024):
    api_key = ensure_api_key(api_key)
    return genai.GenerativeModel(model_name, generation_config={
        "temperature": float(temperature),
        "max_output_tokens": int(max_output_tokens),
    })
