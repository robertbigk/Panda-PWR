"""Init file for PandaPWR integration."""

import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN
from .api import PandaPWRApi

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up PandaPWR from configuration.yaml."""
    _LOGGER.debug("Setting up PandaPWR integration from YAML")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up PandaPWR from a config entry."""
    _LOGGER.debug("Setting up PandaPWR integration from ConfigEntry")
    hass.data.setdefault(DOMAIN, {})

    try:
        # Tworzenie instancji API
        ip_address = entry.data.get("ip_address")
        api = PandaPWRApi(ip_address)
        hass.data[DOMAIN][entry.entry_id] = api
        
        _LOGGER.info(f"PandaPWR integration successfully loaded for entry: {entry.entry_id}")
        await hass.config_entries.async_forward_entry_setups(entry, ["sensor", "binary_sensor", "switch"])
    except Exception as e:
        _LOGGER.error(f"Error during setup of PandaPWR: {e}")
        return False

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.debug("Unloading PandaPWR integration")
    return await hass.config_entries.async_unload_platforms(entry, ["sensor", "binary_sensor", "switch"])
