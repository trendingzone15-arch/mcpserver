import httpx
from app.config.settings import AFTERSHIP_API_KEY, AFTERSHIP_BASE_URL


async def get_tracking_from_aftership(tracking_number: str, slug: str):
    """
    Fetch tracking details from AfterShip using tracking number + courier slug.
    Example:
    tracking_number = "9405511202575421535949"
    slug = "usps"
    """

    headers = {
        "as-api-key": AFTERSHIP_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "tracking_number": tracking_number,
        "slug": slug,
    }

    url = f"{AFTERSHIP_BASE_URL}/trackings"

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()