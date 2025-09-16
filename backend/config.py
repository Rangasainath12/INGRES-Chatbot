# Configurations (DB credentials, API keys)
import os 
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
GeT_gemini_api= os.getenv("GOOGLE_API_KEY")

SARAVAM_API_KEY = os.getenv("SARAVAM_API_KEY")

# DB_HOST = os.getenv("DB_HOST", "localhost")
# DB_NAME = os.getenv("DB_NAME", "water_data_db")
# # DB_USER = os.getenv("DB