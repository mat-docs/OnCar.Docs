# Burst Logging

Burst Logging is the process by which an ECU stores data in [Burst Memory](../logging-memory-allocation.md) while not connected to System Monitor. In some types of ECU, the content of the Burst Memory can be transmitted at intervals using Wide Band Telemetry.

To change the logging configuration in the ECU, you must download it from System Monitor. Similarly, to modify an existing logging configuration in the ECU, that configuration must first be uploaded to System Monitor. See [Loading Configurations](../loading-configurations.md).

When ATLAS reads the data supplied by the ECU, it needs information about the Burst Logging Configuration. System Monitor supplies this information in an export format that ATLAS can read. See [Burst Logging - Export](burst-logging-export.md).

Burst Logging Configuration files can be saved and opened. See [Logging Configuration Files](../logging-configuration-files.md).

## Burst Logging Configuration

To open the Configure Burst Logging dialog box select **Logging** > **Burst Configuration** (CTRL+F1).

!!! note
    If this menu item is not available, you must create a new Burst Logging Configuration file or open an existing one. See [Creating New Files](../../../project-management/files/creating-new-files.md). Burst Logging Configuration is only available if the relevant Customer Base has permission, as set in [Customer Base Advanced Settings](../../../project-management/customer-bases/customer-base-advanced-settings.md).

The dialog box has the following tabs:

- [Parameters](burst-logging-parameters-tab.md) - Select the parameters to be logged and assign them to blocks and intervals.
- [Triggers](burst-logging-triggers-tab.md) - Set the trigger conditions to start and stop data logging.
- [Session](burst-logging-session-tab.md) - Edit the characteristics of the [Session](../sessions-and-telemetry.md) that is created when the contents of the Burst Memory are uploaded or transmitted to ATLAS. This tab is not shown on units whose BIOS configures telemetry.

The title bar displays the name of the Logging Configuration file being edited.

**See also:** [Logging](../index.md); [Logging Memory Allocation](../logging-memory-allocation.md); [Sessions and Telemetry](../sessions-and-telemetry.md); [Loading Configurations](../loading-configurations.md); [Logging Configuration Files](../logging-configuration-files.md); [Wide Band Telemetry](../sessions-and-telemetry.md)
