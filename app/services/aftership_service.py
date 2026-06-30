import httpx

from app.config.settings import SHIPMENT_API_BASE_URL


async def get_tracking_from_shipment_api(tracking_number: str):
    """
    Fetch shipment details from the Shipment API.

    Args:
        tracking_number (str): Shipment tracking number.

    Returns:
        dict: Shipment details.

    Raises:
        httpx.HTTPStatusError: If the API returns an error response.
        httpx.RequestError: If the request cannot be completed.
    """

    url = f"{SHIPMENT_API_BASE_URL}/{tracking_number}"

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)

        response.raise_for_status()

        return response.json()