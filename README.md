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

# Home Automation - Domotique

As a matter of fact, We currently have only a single relay to pilot. It is used to drive the central heating sytem. This is done via a linux cron job that periodically reads some values from the timeserie database, compute some decision tree and publish an on/off value to MQTT. The autonomous Wi-Fi relay subscribe to that MQTT topic and acts accordingly meanwhile reporting its state and other measurements to the remote MQTT broker.

I plan to drive the new infrared heater panels with a similar approach, not relying to any third party home automation software. \
The only usage I forsee so far for such home automation package is ease to acces to some predefined dashboards. I do not think this is enough to deploy such solution(s)...

I would love to add sensors and actuators but lack usefull ideas (or hardware) where automation makes sense for the rented home I live!
