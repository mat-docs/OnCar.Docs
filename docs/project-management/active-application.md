# Active Application

A Project contains one or more Applications. System Monitor controls which applications are affected by various operations, especially those involved in Developing Data Versions.

The applications that are affected are called the Active Applications. The Active Applications are shown in bold in the Parameter Explorer and the ECU Bar.

**Make an Application Active or Inactive:**

1. Select an Application in the Parameter Explorer or the ECU Bar.
2. Select **File** > **Active Application**, or right-click and select **Active Application** from the context menu.

!!! note
    You can only change the status of an Application when Live Updates is off.

The shortcut key Alt+A is used to select Active Applications. Its action depends on where it is used:

- **In the Parameter Explorer or ECU Bar** - Alt+A toggles the Active status of the selected application. If no application is selected, Alt+A has no effect.
- **In the Main Window** - If only one application is Active, Alt+A cycles through the applications, making each one Active in turn. If more than one application is Active, Alt+A has no effect.

Applications can also be set to Read Only using **File** > **Application Read Only** or the Parameter Explorer context menu. An Application that is Active and Read Only cannot be edited, but is included in functions that operate on Active Applications, such as Reprogramming.

**See also:** [Applications](applications.md); [Developing Data Versions](developing-data-versions/index.md); [Parameter Explorer](../using-system-monitor/parameters/parameter-explorer.md); [ECU Bar](../using-system-monitor/tool-and-information-bars/ecu-bar.md)
