# agents/brand_identity_agent.py
import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
configure(api_key=GEMINI_API_KEY)

def generate_brand_name_and_tagline(idea: str) -> dict:
    """
    Generates a brand name and tagline using the Gemini API.
    """
    model = GenerativeModel(model_name="gemini-1.5-pro")
    prompt = f"Generate a catchy brand name and tagline for a startup based on this idea: {idea}"
    
    response = model.generate_content(prompt)
    result = response.text.strip()
    
    return {"brand_identity": result}

