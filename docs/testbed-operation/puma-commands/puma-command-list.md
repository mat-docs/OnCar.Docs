# Puma Command List

The table shows which commands in the PUMA command protocol are supported by System Monitor.

PUMA uses different terminology to System Monitor, so the System Monitor equivalent name is given for each supported command. These are the names shown in the [Testbed Message](../testbed-message.md) window and on the [Testbed Properties - Commands](../testbed-properties/testbed-properties-commands.md) tab.

For more information on each command, see the topic for its **Group**.

| Group | PUMA command | System Monitor command | Measurement mode |
|---|---|---|---|
| [Initialisation](puma-commands-initialisation.md) | Init | Init | Yes |
| | Identify | Identify | Yes |
| [Configuration](puma-commands-configuration.md) | Select Description File and Binary File | Select Project and Embedded Data | Yes |
| [Map (Lookup Table) Manipulation](puma-commands-map-manipulation.md) | Select Lookup Table | Select Map | No |
| | Put Lookup Table to AP-S | Put Map to System Monitor | No |
| | Get Lookup Table from AP-S | Get Map from System Monitor | No |
| | Get Lookup Table Value | Get Map Value | No |
| | Set Lookup Table | Set Map | No |
| | Increase Lookup Table | Increase Map | No |
| [Scalar (Parameter) Manipulation](puma-commands-scalar-manipulation.md) | Get Parameter from AP-S | Get Scalar from System Monitor | No |
| | Set Parameter on AP-S | Set Scalar on System Monitor | No |
| [Data Acquisition](puma-commands-data-acquisition.md) | Parameter for Value Acquisition | Select Parameters for Acquisition | Yes |
| | Switching Offline/Online | Switch Offline/Online | Yes |
| | Get On-line Value | Acquire Parameters | Yes |

All commands are available in **Full-operation** mode.

The following PUMA commands are **not** supported by System Monitor. They receive a *command not available* reply.

| Group | PUMA command |
|---|---|
| Initialisation | Emergency |
| Configuration | Copy Binary File (System Monitor: Copy Embedded Data) |
| | Change Binary Filename (System Monitor: Change Embedded Data Filename) |
| Recording | Define Recording Parameters |
| | Define Trigger Parameters |
| | Activate Recorder |
| | Get Recorder Status |
| | Get Recorder Result Header |
| | Get Recorder File |
| | Save Recorder File |
| | Load Recorder File |
| Miscellaneous | Set Graphic Mode |
| | Reset Device |
| | Set Format |
