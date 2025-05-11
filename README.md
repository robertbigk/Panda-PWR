# Panda PWR Home Assistant Integration

## Original Project
This integration is based on the original Panda PWR integration developed by **juanillo62gm**. You can find the original project on GitHub at the following link:
[Original Panda PWR Integration by juanillo62gm](https://github.com/juanillo62gm/HA-Panda-PWR)

## Overview
This integration allows you to monitor and control the Panda PWR smart plug using Home Assistant. It supports real-time monitoring of voltage, current, power, energy usage, power state, and USB state. Additionally, you can toggle the power and USB states directly from Home Assistant.

### Key Features
- Real-time monitoring of voltage, current, power, and energy usage.
- Control power and USB state through switches.
- Easily integrated with Home Assistant via IP address.
- Uses local polling for data retrieval.

## Installation
1. Download the integration files and place them in the following directory:
   ```
   /config/custom_components/panda_pwr/
   ```
2. Restart Home Assistant to recognize the new integration.
3. Go to **Settings → Devices & Services → Add Integration → Panda PWR**.
4. Enter your device's IP address (e.g., `http://Your_device_ip/update_ele_data`).
5. Complete the setup.

## Verifying Device Status
To manually check the status of your Panda PWR device, open your web browser and visit:
```
http://Your_device_ip/update_ele_data
```
This should display the current status in JSON format, similar to the following:
```
{"countdown_state":0,"auto_poweroff":"0","countdown":"0","voltage":243,"current":0.073269,"power":4,"power_state":1,"usb_state":0,"ele":26.695404}
```

## Available Entities
The integration creates the following entities:
- **Panda PWR Voltage**: Shows the current voltage (V).
- **Panda PWR Current**: Shows the current (A).
- **Panda PWR Power**: Shows the power consumption (W).
- **Panda PWR Energy**: Shows the energy usage (kWh).
- **Panda PWR Power State**: Binary sensor indicating if the power is on.
- **Panda PWR USB State**: Binary sensor indicating if the USB is on.
- **Panda PWR Power Switch**: Allows toggling the power on/off.
- **Panda PWR USB Switch**: Allows toggling the USB on/off.

## Dashboard Example
To visualize the data and control the device, you can use the following YAML for your Home Assistant dashboard:
```yaml
type: entities
title: Panda PWR
entities:
  - entity: sensor.panda_pwr_voltage
  - entity: sensor.panda_pwr_current
  - entity: sensor.panda_pwr_power
  - entity: sensor.panda_pwr_energy
  - entity: binary_sensor.panda_pwr_power_state
  - entity: binary_sensor.panda_pwr_usb_state
  - entity: switch.panda_pwr_power_switch
  - entity: switch.panda_pwr_usb_switch
```

## Screenshots
![Entities View](https://github.com/robertbigk/Panda-PWR/raw/main/pictures/vivaldi_HA3HuSB0Ki.png)
![Integration Details](https://github.com/robertbigk/Panda-PWR/raw/main/pictures/vivaldi_2TanOBLvL1.png)
![Integration Hub](https://github.com/robertbigk/Panda-PWR/raw/main/pictures/vivaldi_dvTpkZC8SX.png)
![Entity Registration](https://github.com/robertbigk/Panda-PWR/raw/main/pictures/BjNbiqsOPg.png)

## Troubleshooting
If the integration does not load correctly:
1. Check your device IP address.
2. Ensure the device is reachable via the web interface.
3. Enable debugging in Home Assistant and review the logs for errors.

## Support
If you encounter any issues, please submit a bug report with your log details.
