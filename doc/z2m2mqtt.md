Another MQTT-based Bash script!

This script appears to be designed to listen to an MQTT broker, filter and transform incoming messages, and then forward the transformed data to another MQTT topic. Here's a breakdown
of what the code does:

1. The script sets some environment variables and defines a few functions:
	* `ctrl_c`: This function handles the Ctrl+C signal, cleaning up and exiting with a status code.
	* `listen`: This is the main listening loop. It reads lines from standard input, extracts relevant information (timestamp, topic, message), filters and transforms the message using `j
`jq`, and then publishes the transformed data to an MQTT topic using `mosquitto_pub`.
2. The script sets up some default values for variables:
	* `MQTT_TOPIC_IN`: The MQTT topic to listen to (default is `zigbee2mqtt`).
	* `MQTT_TOPIC_OUT`: The MQTT topic to publish to (default is `sensors`).
3. The script defines a trap function (`ctrl_c`) that will be triggered when the user presses Ctrl+C.
4. The main loop of the script uses `mosquitto_sub` to subscribe to the specified MQTT topic and its subtopics. The output from `mosquitto_sub` is piped to the `listen` function, which
processes each line.

Some notable features of this script include:

* It uses `jq` to filter and transform incoming messages. This suggests that the script is designed to extract specific information from the MQTT messages and reformat them for further
processing or visualization.
* It uses `mosquitto_pub` to publish transformed data to an MQTT topic. This allows the script to forward the filtered and transformed data to another system or application.
* The script includes some basic error handling, such as printing error messages if the `mosquitto_pub` command fails.

Overall, this script appears to be designed to collect and process IoT device data from an MQTT-based system, transform it into a standardized format, and then forward the transformed
data to another system or application for further analysis or visualization.

`jq` is a lightweight and flexible command-line JSON processor that allows you to work with JSON data in a shell-friendly way. It's often used in combination with other tools, like
`bash`, `awk`, or `sed`, to manipulate, transform, and extract information from JSON data. `jq` is particularly useful when working with JSON data in shell scripts, as it provides a powerful and flexible way to manipulate and extract information from JSON data without having
to write complex parsing code.
