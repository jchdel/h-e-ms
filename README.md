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
Will do a first run from a custom APKOVL and as podman's pod, both on x86 hardware. I have a dozen such x86(_64) boxes lying around from previous project... \
Later on, I will try on Raspberry Pi and other ARM boards I have at the lab (the famous "Armada")...

I would love to add prediction capabilities based on forecasts, previous readings adapted to weather conditions and time of year...

# Hardware

At this time of writing, some sensors are deployed, some still lying in boxes and most not ordered or delivered yet!

What is already in place:
- EmonPi (Raspberry Pi 3 + RF)
- EmonRx (arduino + RF)
- EmonTx x4 (arduino + RF)
- Davis weather station (ethernet)
- Inverter WKS (USB)
- Wifi MQTT relay

What exists but is to be activated:
- (USB21wire)
- (zigbee2mqtt)
- (USB2RJ485-modbus)
- (Pylontech BMS)
- (wind turbine)
- (wind turbine MPPT)

What is ordered but not delivered yet:
- zigbee smart plugs
- Long infrared heating panels

what is whished:
- environemental Davis sensors fully deployed
- window opening zigbee detectors
- more zigbee smart plugs or electric board relays
- zigbee sensors and meters
- zibbee actuators
- rain water storage and filter
- biomethane producing compost
