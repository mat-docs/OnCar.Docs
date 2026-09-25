# Deleting Errors

Errors are held in the ECU in the form of special Measurement Parameters. The flags on these parameters can all be set to zero.

The **Delete Errors** command (F8) on the [ECU Menu](../../../using-system-monitor/menus/ecu-menu.md) sends a message that causes the ECU to delete its internal store of logged Errors. All logged errors are automatically removed from the Error Window as the error flags indicating logged errors are no longer set. Any acknowledgement of errors is also cleared.

- The command only applies to [Active Applications](../../../project-management/active-application.md), and only to controllers that are defined as supporting Delete Errors.
- The command is only available when there is communication with the unit, and is not available when the Advanced Setting **ECU read only mode** (**Tools** > **Advanced Settings**) is on.
- Whether the command is permitted is also controlled by the **Permit delete errors** setting of the relevant [Customer Base](../../../project-management/customer-bases/index.md), set in [Customer Base Advanced Settings](../../../project-management/customer-bases/customer-base-advanced-settings.md). The same setting applies to **Delete Min/Max**.

**See also:** [Error Display](error-display.md); [Measurement Parameters](../../../using-system-monitor/parameters/measurement-parameters.md)
