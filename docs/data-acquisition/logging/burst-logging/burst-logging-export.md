# Burst Logging - Export

When ATLAS reads the data supplied by the ECU, it needs information about the Burst Logging Configuration. System Monitor supplies this information in an export format that ATLAS can read.

A Burst Configuration Export file is created automatically every time a Burst Logging Configuration is downloaded to an ECU (see [Loading Configurations](../loading-configurations.md)). The file name is generated from the timestamp in the ECU. ATLAS uses the file name to link the session to the configuration file, so it must not be changed.

The export files are saved in the folder set by **Directory for exported logging files** in the [Advanced Settings](../../../using-system-monitor/settings.md) dialog box (**Tools** > **Advanced Settings**). If this folder is not defined, the export fails and you are asked to define it.

To create a Burst Configuration Export file at any time, select **Logging** > **Burst Export...**. **Logging** > **Remote Export...** does the same for the Remote Logging Configuration.

**See also:** [Burst Logging](index.md)
