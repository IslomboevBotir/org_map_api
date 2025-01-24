from typing import Mapping

from pydantic import TypeAdapter

from src.serializers.base import BaseListSerializer
from src.entities.organizations import OrganizationsInBuildingSchema
from src.entities.organizations import OrganizationsActivitySchema

organizations_in_building_adapters = TypeAdapter(list[OrganizationsInBuildingSchema])
organizations_activity_adapters = TypeAdapter(list[OrganizationsActivitySchema])


class OrganizationInBuildingSerializer(BaseListSerializer):
    def serializer_list(self, value: Mapping, **kwargs) -> list[OrganizationsInBuildingSchema]:
        return organizations_in_building_adapters.validate_python(value, **kwargs)


class OrganizationsInActivitySerializer(BaseListSerializer):
    def serializer_list(self, value: Mapping, **kwargs) -> list[OrganizationsActivitySchema]:
        return organizations_activity_adapters.validate_python(value, **kwargs)
