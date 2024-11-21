# YAH - yet another HEMS

HEMS: Home Energy Monitoring System

Running on R-Pi 3B+

Alpine Linux, a couple of packages, Python and Bash...

## Architecture

For every supported protocol, sensors and actuators are exposed as MQTT topics by specific daemon.

Agents are listening to specific MQTT topics and take action upon receiving messages. \
Agents feed a key/value store and a timeserie database with collected values. \
They also publish MQTT messages. \
Different agents can read from the key/value store. \
Agents enforcre automations.

Dashboards are build from the timeserie database.

Everything is self hosted! Nothing goes to the cloud!

### Supported protocols

- 1-wire
- Radio Frequency
- Wi-Fi + HTTP
- Modbus (USB)
- Modbus (ethernet)
- Zigbee

## Current automations

- wheather station integration (Davis Vantage Pro)
- night only: some power plugs are deactivated while photo-voltaic is producing (reverse could be true)
- feedback light bulb: a light bulb changes color according to the battery state-of-charge
- thermostats: infra-red heaters are driven according to room temperature, specification and available energy
- generator/utility start request: when battery state-of-charge is too low
- power and energy consumption and production analysis (utility, solar, battery, load)
- manage solar forecast (subscription to external service)

### Planned automations

- garden monitoring
- garden watering
- motion/presence detection for scene activation
- garden lightning
- water monitoring (drinkable and rain captation)
- air quality monitoring

mostly waiting for the gadgets...
