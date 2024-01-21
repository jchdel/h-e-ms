# h(e)ms

Home (Energy) Monitoring System

A DIM (do-it-myself) project...

I want a cheap generic IoT edge device with local analytical features.

Come to mind:
- MQTT broker
- logrotate
- influxDB
- mqtt2influxdb
- zigbee2mqtt (smart plugs)
- emonHub (RF2mqtt)
- mqtt-wifi-relay (to pilot the heater)
- 1wire2mqtt (temperature and reeds relays)
- grafana (from influxdb)
- nginx (reverse proxy grafana with encryption and authentication)
- letsencrypt (certs management)
- davis2mqtt (weather station)
- inverter2mqtt (WKS)
- bms2mqtt (pylontech)
- collectd (2influxdb)
- ...

I guess an Alpine Linux running in RUN-FROM-RAM mode will fit the bill as operating system. If not, I will use some Debian derivative. \
Will do a first run from a custom APKOVL and as podman's pod, both on x86 hardware. I have a dozen such x86_64 boxes lying around from previous project... \
Later on, I will try on Raspberry Pi and other ARM boards I have at the lab (the famous "Armada")...

I would love to add prediction capabilities based on forecasts, previous readings adapted to weather conditions and time of year...

# Hardware

Inventory:
- EmonPi (Raspberry Pi 3 + RF + WiFi + ehernet + USB)
- EmonTh (arduino + RF)
- EmonTx x4 (arduino + RF)
- Davis weather station (ethernet)
- Inverter WKS (USB)
- MQTT relay (WiFi)
- Toon (WiFi)
- zigbee USB
- zigbee smart plugs
- one-wire USB
- RS485 USB
- x86_64: 2GB ram; 32GB HDD; 2x eth; WiFi; 4G; 2x USB; 2x RS485; 2x DIO; rail DIN
- Raspberry Pi 3
- Solar Pannels
- Battery 48V
- Wind Turbine + inverter

# Home Automation - Domotique

