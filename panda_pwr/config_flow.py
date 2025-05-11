"""Config flow for PandaPWR integration."""

import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN
from .api import PandaPWRApi

_LOGGER = logging.getLogger(__name__)

class PandaPWRConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for PandaPWR."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            ip_address = user_input[CONF_IP_ADDRESS]
            _LOGGER.debug(f"Attempting to connect to Panda PWR at {ip_address}")

            try:
                api = PandaPWRApi(ip_address)
                if await api.test_connection():
                    _LOGGER.info("Connection to Panda PWR successful.")
                    return self.async_create_entry(title="Panda PWR", data=user_input)
                else:
                    _LOGGER.error("Unable to connect to Panda PWR.")
                    errors["base"] = "cannot_connect"
            except Exception as e:
                _LOGGER.error(f"Unexpected exception: {e}")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required(CONF_IP_ADDRESS): str}),
            errors=errors,
        )
