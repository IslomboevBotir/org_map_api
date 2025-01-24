from pydantic import BaseModel


class OrganizationsInBuildingSchema(BaseModel):
    address: str
    name: str


class OrganizationsActivitySchema(BaseModel):
    name: str


class OrganizationSchema(BaseModel):
    name: str
