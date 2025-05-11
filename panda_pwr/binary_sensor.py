"""Binary sensor platform for PandaPWR integration in Home Assistant."""

from typing import Any
import logging

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities) -> None:
    """Set up the binary sensor platform for PandaPWR."""
    api = hass.data[DOMAIN][entry.entry_id]
    sensors = [
        PandaPWRBinarySensor(api, entry, "power_state", "Power State"),
        PandaPWRBinarySensor(api, entry, "usb_state", "USB State"),
    ]
    async_add_entities(sensors, update_before_add=True)

class PandaPWRBinarySensor(BinarySensorEntity):
    def __init__(self, api: Any, entry: ConfigEntry, key: str, name: str) -> None:
        self._api = api
        self._key = key
        self._attr_name = f"Panda PWR {name}"
        self._attr_unique_id = f"panda_pwr_{key}"
        self._attr_is_on = False

    async def async_update(self) -> None:
        try:
            data = await self._api.get_data()
            if data and self._key in data:
                self._attr_is_on = bool(data[self._key])
                _LOGGER.debug(f"{self._attr_name} updated: {self._attr_is_on}")
            else:
                _LOGGER.error(f"Data key '{self._key}' not found in API response: {data}")
        except Exception as e:
            _LOGGER.error(f"Error updating {self._attr_name}: {e}")
