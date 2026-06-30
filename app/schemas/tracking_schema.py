from pydantic import BaseModel
from typing import List, Optional


class CustomerSchema(BaseModel):
    customerId: str
    name: str
    phone: str
    email: str


class LiveLocationSchema(BaseModel):
    latitude: float
    longitude: float
    address: str
    speed: Optional[float] = None
    heading: Optional[str] = None
    lastUpdated: str

class TrackingHistorySchema(BaseModel):
    status: str
    timestamp: str
    location: str
    latitude: float
    longitude: float
    description: str


class DestinationSchema(BaseModel):
    latitude: float
    longitude: float


class MapSchema(BaseModel):
    googleMapsUrl: str
    destination: DestinationSchema


class ShipmentDataSchema(BaseModel):
    shipmentId: str
    trackingNumber: str
    orderId: str

    status: str
    statusCode: str

    estimatedDelivery: Optional[str] = None

    customer: CustomerSchema

    liveLocation: LiveLocationSchema

    trackingHistory: List[TrackingHistorySchema]

    map: MapSchema



class TrackingResponseSchema(BaseModel):
    success: bool

    tool: Optional[str] = "get_tracking"

    message: Optional[str] = None

    timestamp: Optional[str] = None

    data: Optional[ShipmentDataSchema] = None

