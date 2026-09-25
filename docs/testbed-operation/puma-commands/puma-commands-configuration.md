# Puma Commands – Configuration

| System Monitor command | PUMA command | Function |
|---|---|---|
| Select Project and Embedded Data | Select Description File and Binary File | PUMA supplies: <br>- the name of the System Monitor project file <br>- the name of the embedded data file with which it wants to work. <br>System Monitor records the file names, shows them in the [Testbed Message](../testbed-message.md) window and returns a LUN of 1 to PUMA. The files are not opened, and the names are not checked against the Project open in System Monitor. <br>Only one project and embedded data file may be selected at a time. Available in both Measurement and Full-operation modes. |

The PUMA **Copy Binary File** (Copy Embedded Data) and **Change Binary Filename** (Change Embedded Data Filename) commands are not supported. System Monitor replies to them with *command not available*. To save the edit buffer to a data version, use System Monitor directly.

**See also:** [Puma Command List](puma-command-list.md); [Puma Errors](puma-errors.md)
