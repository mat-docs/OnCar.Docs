# External Inputs Configuration

The External Inputs Configuration tool allows sensor inputs to be configured and [calibration data](../software-calibrated-sensors/index.md) to be applied to sensors connected to the ECU.

External Inputs Configuration operates on sensors that are not defined in the Program Version. Use [Sensors & Actuators](../sensors-and-actuators/index.md) for sensors and actuators that are defined in the Program Version. It is used to configure sensors on the [TAG Sensor Bus](../../../hardware/sensor-bus.md) and sensors connected directly to the unit. CAN links are configured with [CAN Configuration](../../logging/can-configuration/can-configuration-dialog-box/index.md).

To open the External Inputs dialog box select **Sensors** > **External Inputs Configuration...**.

!!! note
    If this menu item is not available, select **File** > **New** and then select External Inputs Config from the list of documents in the File New dialog box. External Inputs configuration files have the extension .xic. External Inputs Configuration is only available if the relevant Customer Base has permission, as set in [Customer Base Advanced Settings](../../../project-management/customer-bases/customer-base-advanced-settings.md).

To change the External Inputs configuration in the ECU, you must download it from System Monitor (**Sensors** > **External Inputs Download...**, CTRL+F10). Similarly, to modify an existing External Inputs configuration in the ECU, it must first be uploaded to System Monitor (**Sensors** > **External Inputs Upload...**, CTRL+ALT+F10). See [Loading Configurations](../../logging/loading-configurations.md).

The External Inputs parameters are shown in the [Parameter Explorer](../../../using-system-monitor/parameters/parameter-explorer.md).

Configuring a DATALab system requires the following steps:

1. [Select an Input Source](external-inputs-input-source.md)
2. [Select a Bus](external-inputs-selecting-a-bus.md)
3. [Select a Node](external-inputs-selecting-a-node.md)
4. [Add Sensors](external-inputs-adding-a-sensor.md)

Repeat these steps as required until the system is fully configured. Click **Apply** to apply changes without closing the dialog box. The configuration can then be sent to the ECU and/or saved as a file.

Right-click an item in the tree for the following commands: **Show Unconfigured Items**, **Cut**, **Copy**, **Paste**, **Delete** and **Information**.

**See also:** [External Inputs - Drag and Drop](external-inputs-drag-and-drop.md); [External Inputs - Input Source](external-inputs-input-source.md); [Parameter Explorer](../../../using-system-monitor/parameters/parameter-explorer.md); [Program Version](../../../project-management/program-and-data-versions/index.md); [Sensors](../index.md)
