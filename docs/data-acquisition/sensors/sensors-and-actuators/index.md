# Sensors & Actuators

Sensors & Actuators allows you to apply calibration data to sensors, to enable and disable individual sensors and to enter values for sensor constants. Sensors & Actuators operates on sensors and actuators defined in the Program Version.

!!! note
    Use [External Inputs Configuration](../external-inputs/external-inputs-configuration.md) for sensors that are not defined in the Program Version.

The Sensors & Actuators commands are on the [Sensors Menu](../../../using-system-monitor/menus/sensors-menu.md):

| Command | Description |
|---|---|
| **Open Sensor Set** (CTRL+F11) | Opens the sensor set that was last open in the current project. |
| **Sensor Set Download** (CTRL+F12) | Downloads the sensor set to the ECU. |
| **Sensor Set Upload** (CTRL+ALT+F12) | Uploads the sensor set from the ECU. |
| **Sensor Set Upload New** | Uploads the sensor set from the ECU into a new sub set. |
| **Enable / Disable** | Opens the [Enable/Disable Sensors](enabling-and-disabling-sensors-and-actuators.md) dialog box. |
| **Force Rebuild Sensor Database** | Forces the binary sensor calibration file to be rebuilt the next time it is needed (see [Calibration Files](../software-calibrated-sensors/calibration-files.md)). |

!!! note
    Sensors & Actuators is only available if the relevant Customer Base has permission, as set in [Customer Base Advanced Settings](../../../project-management/customer-bases/customer-base-advanced-settings.md).

Before Sensors & Actuators can be used, a Sensor Set must be associated with the Project. See [Sensor Sets](sensor-sets.md).

**See also:** [Program Version](../../../project-management/program-and-data-versions/index.md); [Sensors & Actuators dialog box](sensors-and-actuators-dialog-box.md); [Sensors](../index.md); [Sensor Sets](sensor-sets.md); [Software Calibrated Sensors](../software-calibrated-sensors/index.md)
