from pydantic import BaseModel
from typing import Optional


class LastCheckpointSchema(BaseModel):
    message: Optional[str] = None
    location: Optional[str] = None
    checkpoint_time: Optional[str] = None


class TrackingResponseSchema(BaseModel):
    success: bool
    tracking_number: str
    tracking_id: Optional[str] = None
    status: Optional[str] = None
    subtag: Optional[str] = None
    courier: Optional[str] = None
    eta: Optional[str] = None
    last_checkpoint: Optional[LastCheckpointSchema] = None
    message: Optional[str] = None