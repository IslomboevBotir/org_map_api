from pydantic import BaseModel


class OrganizationByActivitySchema(BaseModel):
    organization_id: int
    organization_name: str
