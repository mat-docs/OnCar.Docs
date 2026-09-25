# Requirements

The **Dashboard** command in the **Desktop** > **Window** sub-menu is only available when all of the following are true:

- The project's main ECU is a PCU-400, that is, one of the loaded [Applications](../project-management/applications.md) (.pgv files) is intended for use with the PCU.
- The current Desktop page is not locked.
- No PCU Dash Configuration window is already open. Only one PCU Dash Configuration window can be open at a time.

The Measurement Parameters available for use with the PCU Application are defined in the .pgv file. If required, they can also be selected for other data displays in System Monitor. However, tuning operations with Editable Parameters cannot be carried out in the PCU Application.

To download a configuration to the display unit, System Monitor must be communicating with the car. See [Dash Configuration Main Menu](pcu-dasbboard-window/dash-configuration-main-menu.md).

!!! note
    The menu shows **Alt+Shift+D** beside **Dashboard**, but that key clears the display offsets on the current Page. Use the menu to open the PCU Dash Configuration window. See [Keyboard Operation](../using-system-monitor/keyboard-operation.md).
