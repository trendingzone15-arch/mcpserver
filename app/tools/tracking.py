from app.services.aftership_service import get_tracking_from_aftership
from app.schemas.tracking_schema import TrackingResponseSchema, LastCheckpointSchema


async def get_tracking(tracking_number: str, slug: str):
    try:
        data = await get_tracking_from_aftership(
            tracking_number=tracking_number,
            slug=slug
        )

        # AfterShip response structure
        tracking = data.get("data", {}).get("tracking", {})

        checkpoints = tracking.get("checkpoints", [])
        latest_checkpoint = checkpoints[0] if checkpoints else {}

        response = TrackingResponseSchema(
            success=True,
            tracking_number=tracking.get("tracking_number") or tracking_number,
            tracking_id=tracking.get("id"),
            status=tracking.get("tag"),
            subtag=tracking.get("subtag"),
            courier=tracking.get("slug"),
            eta=tracking.get("expected_delivery"),
            last_checkpoint=LastCheckpointSchema(
                message=latest_checkpoint.get("message"),
                location=latest_checkpoint.get("location"),
                checkpoint_time=latest_checkpoint.get("checkpoint_time"),
            ),
        )

        return response.model_dump()

    except Exception as e:
        return TrackingResponseSchema(
            success=False,
            tracking_number=tracking_number,
            message=f"Failed to fetch tracking details: {str(e)}"
        ).model_dump()