"""API module for PandaPWR integration."""

import logging
import aiohttp
import async_timeout

_LOGGER = logging.getLogger(__name__)

class PandaPWRApi:
    def __init__(self, ip_address: str):
        self._base_url = f"http://{ip_address}"
        _LOGGER.debug(f"API initialized with base URL: {self._base_url}")

    async def get_data(self) -> dict:
        """Fetch data from the device."""
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(10):
                    async with session.get(f"{self._base_url}/update_ele_data") as response:
                        if response.status == 200:
                            data = await response.json()
                            _LOGGER.debug(f"Received data: {data}")
                            return data
                        _LOGGER.error(f"Failed to fetch data, status: {response.status}")
                        return {}
        except Exception as e:
            _LOGGER.error(f"Error fetching data from device: {e}")
            return {}

    async def test_connection(self) -> bool:
        """Test the connection to the device."""
        try:
            data = await self.get_data()
            return bool(data)
        except Exception as e:
            _LOGGER.error(f"Connection test failed: {e}")
            return False
