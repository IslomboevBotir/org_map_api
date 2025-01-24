from typing import Mapping

from pydantic import TypeAdapter

from src.serializers.base import BaseListSerializer
from src.entities.activity import OrganizationByActivitySchema

organization_by_activity_type_adapter = TypeAdapter(list[OrganizationByActivitySchema])


class OrganizationByActivitySerializer(BaseListSerializer):
    def serializer_list(self, value: Mapping, **kwargs) -> list[OrganizationByActivitySchema]:
        return organization_by_activity_type_adapter.validate_python(value, **kwargs)
