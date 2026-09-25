# Calibration Files

The [Sensor PRM](../../../project-management/files/types-of-files/ecu-files.md) file lists the sensor types and their ASCII (.dat) [sensor calibration](../obtaining-sensor-calibration-data/index.md) files. System Monitor uses the conversion utility TpSbinary.exe to convert the latest .dat data into a binary calibration file (.bcf), which it reads. The name and location of the Sensor PRM file is set by **File for sensor calibration** in the [Advanced Settings](../../../using-system-monitor/settings.md) dialog box.

## Features

- The binary calibration file has the same name as the .prm file but with the extension .bcf.
- When data is downloaded to the ECU, a sensor configuration created from the .bcf file is also downloaded.
- If the .prm file or any of the .dat files are newer than the .bcf file, TpSbinary is run to update the .bcf file when the calibration data is next needed.
- **Sensors** > **Force Rebuild Sensor Database** deletes the .bcf file so that it is rebuilt the next time it is needed, regardless of the file dates. The menu item is shown checked while a rebuild is pending.
- If TpSbinary.exe or a calibration file cannot be found, or TpSbinary fails to create the .bcf file, an error message is displayed.

## File structure

TpSbinary requires the following file structure:

- TpSbinary.exe must be in the same folder as the Sensor PRM file.
- You must have write access to that folder, so that TpSbinary can create temporary files.
- The .dat calibration files are placed in sub-folders below the folder containing TpSbinary.exe and the Sensor PRM file.
- The names of the .dat files, and of the folders that contain them, must follow the DOS 8.3 naming rules. Long names must not be used.

!!! note
    Ensure that **File for sensor calibration** in Advanced Settings points to the Sensor PRM file in the folder where TpSbinary is installed.

**See also:** [Advanced Settings](../../../using-system-monitor/settings.md); [ECU Files](../../../project-management/files/types-of-files/ecu-files.md); [Obtaining Sensor Calibration Data](../obtaining-sensor-calibration-data/index.md); [Sensors & Actuators](../sensors-and-actuators/index.md); [Software Calibrated Sensors](index.md)
