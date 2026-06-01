# IoT Data Logging — Industrial Sensor Monitor

## Project Overview
A real-time sensor monitoring system that simulates industrial pump data, transmits it over MQTT, detects temperature anomalies, and logs every reading with a timestamp. Built to demonstrate the core data pipeline used in industrial IoT environments.

## Architecture
`publish.py (simulated sensor)` → `Mosquitto MQTT Broker` → `pump.py (subscriber)` → `pump_log.txt`

## Technologies Used
- Python 3
- paho-mqtt
- Mosquitto MQTT Broker

## How to Run
1. Install dependency: `pip install paho-mqtt`
2. Start Mosquitto broker locally
3. Run subscriber: `python pump.py`
4. Run publisher in second terminal: `python publish.py`

## What It Demonstrates
- MQTT publish/subscribe communication
- JSON payload parsing
- Threshold-based alert logic
- Timestamped persistent logging
