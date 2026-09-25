# Diagnostics

Diagnostics provides information for embedded software developers and can be useful for troubleshooting the operation of the ECU and of System Monitor itself.

The Diagnostics tools are on the **Tools** menu:

| Command | Description | Available when |
|---|---|---|
| [Read RAM](../ecu-control/ecu-memory/read-ram.md) (ALT+R) | Opens a window that displays the content of the memory for a particular controller in the attached ECU. | A Desktop is open |
| [Single Message](../ecu-control/single-message.md) (ALT+M) | Allows messages to be sent to the ECU and the response to be viewed. | A Project is open |
| [Force Complete Reprogram](../ecu-control/ecu-memory/force-complete-reprogram.md) (ALT+C) | Downloads all the data and code for the ECU whether it has changed or not. | Communications with the ECU are enabled |

**Single Message** and **Force Complete Reprogram** are not available when the **ECU read only mode (Y/N)** [Advanced Setting](../using-system-monitor/settings.md) is on. See [ECU On-Line](../ecu-control/ecu-on-line.md).

**See also:** [Developer Functions](index.md); [ECU Control](../ecu-control/index.md)
