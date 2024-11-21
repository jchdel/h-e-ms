Heating is mostly provided by (long) infra-red panels driven by a zigbee smart plug.

A room with such heater also has a zigbee temperature and humidity sensor.

An hard limit is enforced for current used for heating.

Every time a temperature is published, an agent checks if room temperature is below configured threshold and if there is available power in the heating pool and drives related heater accordingly.

One helper function computes availaible power.

Each room can be configured to have time ranges of higher temperature needs.
