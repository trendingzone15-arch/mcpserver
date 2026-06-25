import os
from dotenv import load_dotenv

load_dotenv()

AFTERSHIP_API_KEY = os.getenv("AFTERSHIP_API_KEY")
AFTERSHIP_BASE_URL = os.getenv(
    "AFTERSHIP_BASE_URL",
    "https://api.aftership.com/tracking/2026-01"
)