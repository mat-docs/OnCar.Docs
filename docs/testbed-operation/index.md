# Testbed Operation

System Monitor can be used with an AVL PUMA testbed system for unattended [Tuning](../tuning/index.md).

The PUMA interface complies with [ASAP3](../project-management/asap-compatibility.md) and is described in detail in:

- AVL ECU Application System Interface - Implementation >SERIAL= V1.0
- AVL ECU Application System Interface - V2.0 Serial (Translation)

The PUMA system communicates with System Monitor via a serial port (RS-232) or over TCP/IP. See [Testbed Properties - Link](testbed-properties/testbed-properties-link.md).

PUMA uses a software protocol to issue [Commands](puma-commands/index.md) to System Monitor and receive replies. The commands allow PUMA to:

- Read and change the values of Editable Parameters
- Download the values of Editable Parameters to the ECU
- Specify a set of Measurement Parameters and acquire their values
- Nominate a parameter description file and a binary data file. In System Monitor, the parameter description is part of a Project and binary data is part of an Embedded Data file.

!!! note
    The combination of System Monitor and PUMA can only work with one project (description) and one embedded data (binary) file at a time.

## Testbed commands

Select **Tools** > **Testbed** to access the Testbed submenu. Availability of the Testbed commands depends on your System Monitor licence.

| Command | Description |
|---|---|
| **Configure** | Opens the [Testbed Properties](testbed-properties/index.md) dialog box (shortcut CTRL+SHIFT+F5). Not available while the Testbed Link is enabled. |
| **Enable Link** | Switches the [Testbed Link](testbed-link.md) on and off (shortcut CTRL+SHIFT+F6). |
| **Message Window** | Opens and closes the [Testbed Message](testbed-message.md) window (shortcut CTRL+SHIFT+F7). |

**See also:** [Editable Parameters](../using-system-monitor/parameters/editable-parameters.md); [Measurement Parameters](../using-system-monitor/parameters/measurement-parameters.md); [Puma Commands](puma-commands/index.md); [Tuning](../tuning/index.md)
