from datetime import datetime

from app.services.aftership_service import get_tracking_from_shipment_api

from app.schemas.tracking_schema import (
    TrackingResponseSchema,
    ShipmentDataSchema,
)


async def get_tracking(tracking_number: str):
    """
    Fetch shipment tracking details.

    Args:
        tracking_number (str): Shipment tracking number.

    Returns:
        dict: Standardized tracking response.
    """

    try:
        response = await get_tracking_from_shipment_api(
            tracking_number=tracking_number
        )

        shipment = response.get("data")

        if not shipment:
            return TrackingResponseSchema(
                success=False,
                tool="get_tracking",
                message="Tracking information not found.",
                timestamp=datetime.utcnow().isoformat() + "Z",
            ).model_dump()

        return TrackingResponseSchema(
            success=True,
            tool="get_tracking",
            message="Shipment tracking retrieved successfully.",
            timestamp=datetime.utcnow().isoformat() + "Z",
            data=ShipmentDataSchema(**shipment),
        ).model_dump()

    except Exception as e:

        return TrackingResponseSchema(
            success=False,
            tool="get_tracking",
            message=f"Failed to fetch tracking details: {str(e)}",
            timestamp=datetime.utcnow().isoformat() + "Z",
        ).model_dump()