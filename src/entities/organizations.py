from pydantic import BaseModel


class OrganizationsInBuildingSchema(BaseModel):
    address: str
    name: str


class OrganizationsActivitySchema(BaseModel):
    name: str


class OrganizationSchema(BaseModel):
    name: str


class OrganizationNearbyQueryParamsSchema(BaseModel):
    lat: float
    lon: float
    radius: float


class OrganizationInAreaQueryParamsSchema(BaseModel):
    lat1: float
    lon1: float
    lat2: float
    lon2: float
