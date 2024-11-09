from pydantic import BaseModel

# Schema for creating new network data entry
class NetworkDataCreate(BaseModel):
    time: str  # Accept time as a string (ISO 8601 format or any string format)
    source_ip: str
    destination_ip: str
    protocol: str

# Schema for returning network data entry with ID and timestamp
class NetworkData(BaseModel):
    id: int
    time: str  # Time is now returned as a string
    source_ip: str
    destination_ip: str
    protocol: str

    class Config:
        orm_mode = True