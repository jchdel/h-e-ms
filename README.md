# YAH - yet another HEMS

HEMS: Home Energy Monitoring System

Running on R-Pi 3B+

Alpine Linux, a couple of packages, Python and Bash...

## Architecture

Sensors and actuators are exposed as MQTT topics.

Daemons expose collected values as sensors.

Agents are listening to specific MQTT topics and take action upon receiving messages. 

Agents feed a key/value store and a timeserie database with collected values. They also publish MQTT messages.

Different agents can read from the key/value store.

Agents enforcre automations.

Dashboards are build from the timeserie database.
