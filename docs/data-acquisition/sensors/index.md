# Sensors

A Sensor is a device that converts a physical property (such as pressure or temperature) into an electrical signal that can be logged. Most Measurement Parameters are the output of a Sensor.

System Monitor has the following facilities to configure the way that Sensors are used. Most are on the [Sensors Menu](../../using-system-monitor/menus/sensors-menu.md):

- [Sensors & Actuators](sensors-and-actuators/index.md) - Used to apply calibration data to sensors, enable or disable individual sensors and enter values for sensor constants. Used on sensors and actuators defined in the Program Version.
- [External Inputs Configuration](external-inputs/external-inputs-configuration.md) - Used to configure sensor inputs and apply calibration data to sensors connected to the ECU through the TAG Sensor Bus or directly to the unit. Used on sensors that are not defined in the Program Version. CAN links are configured with [CAN Configuration](../logging/can-configuration/can-configuration-dialog-box/index.md).
- [Sensor Calibration Tool](software-calibrated-sensors/sensor-calibration-tool.md) - Used to view and edit sensor calibration curves.
- [Input Signal Configuration Tool](external-inputs/input-signal-configuration-tool.md) - Used to configure the scaling of analogue and digital input signals on units that support it (on the Logging menu).

The Sensors menu also has commands to edit, export and import the sensors in a Data Version (**Edit Sensors in Data Version...**, **Export Sensors from Data Version...**, **Import Sensors to Data Version...**) and to synchronise the Data Version with the sensor calibration database (**Synchronise Calibration Data**).

**See also:** [Calibration data](software-calibrated-sensors/index.md); [Data Acquisition](../index.md); [Measurement Parameters](../../using-system-monitor/parameters/measurement-parameters.md); [Software Calibrated Sensors](software-calibrated-sensors/index.md); [Program Versions](../../project-management/program-and-data-versions/index.md)
