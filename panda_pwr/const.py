"""Constants for the PandaPWR integration."""

DOMAIN = "panda_pwr"
CONF_IP_ADDRESS = "ip_address"
DEFAULT_NAME = "Panda PWR"
DEFAULT_PORT = 80
DEFAULT_TIMEOUT = 10
PLATFORMS = ["sensor", "binary_sensor", "switch"]

# Log messages
LOG_INIT = "Initializing Panda PWR integration"
LOG_SETUP = "Setting up Panda PWR component"
LOG_SETUP_ENTRY = "Setting up Panda PWR from config entry"
LOG_CONNECTION_SUCCESS = "Successfully connected to Panda PWR device"
LOG_CONNECTION_FAILED = "Failed to connect to Panda PWR device"
LOG_DATA_FETCHED = "Data fetched from Panda PWR: %s"
LOG_ERROR_FETCH = "Error fetching data from Panda PWR: %s"
