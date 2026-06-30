import os
from dotenv import load_dotenv

load_dotenv()

SHIPMENT_API_BASE_URL = os.getenv(
    "SHIPMENT_API_BASE_URL",
)
ALLOWED_ORIGIN = os.getenv(
    "ALLOWED_ORIGIN",
)