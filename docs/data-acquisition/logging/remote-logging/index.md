# Remote Logging

Remote Logging is the process by which an ECU stores data in [DATALab Memory](../logging-memory-allocation.md) while not connected to System Monitor.

System Monitor is used to edit the logging configuration for the ECU. To change the logging configuration in the ECU, you must download it from System Monitor. Similarly, to modify an existing logging configuration in the ECU, that configuration must first be uploaded to System Monitor. See [Loading Configurations](../loading-configurations.md).

Remote Logging Configuration files (.rlc) can also be saved and opened. See [Logging Configuration Files](../logging-configuration-files.md).

## Configure Remote Logging

Remote Logging is configured in the Configure Remote Logging dialog box. To open the dialog box, select **Logging** > **Remote Configuration** (CTRL+F5).

!!! note
    If the Remote Configuration menu item is not available, you must create a new Remote Logging Configuration file or open an existing one. See [Creating New Files](../../../project-management/files/creating-new-files.md). Remote Logging Configuration is only available if the relevant [Customer Base](../../../project-management/customer-bases/index.md) has permission, as set in [Customer Base Advanced Settings](../../../project-management/customer-bases/customer-base-advanced-settings.md).

The dialog box has the following tabs:

- [Channel Overview](configure-remote-logging-dialog-box/channel-overview-tab.md) - Define the characteristics of the channels used to store data in the ECU.
- **Session** - Edit the [Session Details](../session-details.md). This tab is not shown on units whose BIOS configures telemetry; the session details are then configured in the Data Version.

The dialog box is resizable and the title bar displays the name of the Logging Configuration file being edited.

To compare the configuration with another remote logging configuration file and merge differences, see [Remote Configuration Compare](../remote-configuration-compare/index.md).

**See also:** [Logging](../index.md); [Logging Memory Allocation](../logging-memory-allocation.md); [Sessions and Telemetry](../sessions-and-telemetry.md); [Loading Configurations](../loading-configurations.md); [Logging Configuration Files](../logging-configuration-files.md)
