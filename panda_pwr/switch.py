"""Switch platform for PandaPWR integration in Home Assistant."""

from typing import Any
import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities) -> None:
    """Set up the switch platform for PandaPWR."""
    api = hass.data[DOMAIN][entry.entry_id]
    switches = [
        PandaPWRSwitch(api, entry, "power_state", "Power Switch"),
        PandaPWRSwitch(api, entry, "usb_state", "USB Switch"),
    ]
    async_add_entities(switches, update_before_add=True)

class PandaPWRSwitch(SwitchEntity):
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

    async def async_turn_on(self, **kwargs: Any) -> None:
        _LOGGER.debug(f"Turning on {self._attr_name}")
        await self._api.set_power_state(True)
        self._attr_is_on = True

    async def async_turn_off(self, **kwargs: Any) -> None:
        _LOGGER.debug(f"Turning off {self._attr_name}")
        await self._api.set_power_state(False)
        self._attr_is_on = False
