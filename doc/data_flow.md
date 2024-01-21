"Things" are reading sensors and pushing values to MQTT broker. This is done from zigbee2mqtt, EmonHub, 1wire2mqtt, ...

Some MQTT listeners expose those "inputs" that can the be either manipulated and/or becoming "feeds" to be stored in timeserie databases (EmonCMS, influxDB, timescaleDB, ...).

Business Intelligence can process those timeserie values as it see fit. Then produce valuable reports and dashboards (EmonCMS, grafana, ...).

Home automation may also make use of the values either spot or in a time frame and publish orders to MQTT enabled actuators.
