import pytest
from httpx import Response, AsyncClient
from fastapi import status

from test.constants.activities.mock_data import activity_mock_create_payload_data, activity_mock_update_payload_data


class TestActivitiesFlow:
    @pytest.mark.asyncio
    async def test_create_activities(self, test_client: AsyncClient):
        response: Response = await test_client.post(
            "/api/activities/", json=activity_mock_create_payload_data
        )
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.asyncio
    async def test_get_activity(self, test_client: AsyncClient):
        response: Response = await test_client.get(
            f"/api/activities/{activity_mock_create_payload_data.get("id")}/"
        )
        assert response.status_code == status.HTTP_200_OK
        data: dict = await response.json()
        assert data["id"] == activity_mock_create_payload_data["id"]
        assert data["name"] == activity_mock_create_payload_data["name"]
        assert data["parent_id"] == activity_mock_create_payload_data["parent_id"]

    @pytest.mark.asyncio
    async def test_update_activity(self, test_client: AsyncClient):
        response: Response = await test_client.put(
            f"/api/activities/{activity_mock_create_payload_data.get("id")}/",
            json=activity_mock_update_payload_data
        )
        assert response.status_code == status.HTTP_200_OK
        data: dict = await response.json()
        assert data["name"] == activity_mock_update_payload_data["name"]

    @pytest.mark.asyncio
    async def test_delete_activity(self, test_client: AsyncClient):
        response: Response = await test_client.delete(
            f"/api/activities/{activity_mock_create_payload_data.get("id")}/",
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
