import pytest
from httpx import Response, AsyncClient
from fastapi import status

from test.constants.building.mock_data import building_mock_create_payload_data, building_mock_update_payload_data


class TestBuildingFlow:
    @pytest.mark.asyncio
    async def test_create_building(self, test_client: AsyncClient):
        response: Response = await test_client.post(
            "/api/buildings/", json=building_mock_create_payload_data
        )
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.asyncio
    async def test_get_building(self, test_client: AsyncClient):
        response: Response = await test_client.get(
            f"/api/buildings/{building_mock_create_payload_data.get('id')}/"
        )
        assert response.status_code == status.HTTP_200_OK
        data: dict = await response.json()
        assert data["address"] == building_mock_create_payload_data["address"]
        assert data["location"] == building_mock_create_payload_data["location"]

    @pytest.mark.asyncio
    async def test_update_building(self, test_client: AsyncClient):
        response: Response = await test_client.put(
            f"/api/buildings/{building_mock_create_payload_data.get('id')}/",
            json=building_mock_update_payload_data
        )
        assert response.status_code == status.HTTP_200_OK
        data: dict = await response.json()
        assert data["address"] == building_mock_update_payload_data["address"]

    @pytest.mark.asyncio
    async def test_delete_building(self, test_client: AsyncClient):
        response: Response = await test_client.delete(
            f"/api/buildings/{building_mock_create_payload_data.get('id')}/",
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
