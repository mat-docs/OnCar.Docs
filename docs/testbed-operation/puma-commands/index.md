# Puma Commands

System Monitor implements a limited set of commands from the PUMA protocol V2.0, as listed in the [Puma Command List](puma-command-list.md). There is no support for V1.0 or any of its later sub-versions.

For more detailed descriptions of the standard PUMA commands, refer to:

- AVL ECU Application System Interface - Implementation >SERIAL= V1.0
- AVL ECU Application System Interface - V2.0 Serial (Translation)

In all commands, engineering units are used for the values of the following:

- Measurement parameters
- Editable parameters
- Map breakpoints
- Plausible physical limits
- Minimum increments

## Command sequence

- Until PUMA sends **Init**, System Monitor ignores all other commands.
- After **Init**, PUMA must send **Identify**. Until a successful **Identify** has been received, System Monitor replies to every other command with *command not executed*.
- In **Measurement** mode (see [Testbed Properties - Link](../testbed-properties/testbed-properties-link.md)), only the Initialisation, **Select Project and Embedded Data** and Data Acquisition commands are accepted. The Scalar and Map commands receive a *command not available* reply.
- Commands that System Monitor does not support receive a *command not available* reply.
- Each command is checked against its checksum. If the checksum is wrong, System Monitor replies with *error during execution* ("Invalid checksum").

If identifier translation is enabled (see [Testbed Properties - Translate](../testbed-properties/testbed-properties-translate.md)), the parameter and map identifiers sent by PUMA are translated to System Monitor identifiers before they are used.

**See also:** [Testbed Operation](../index.md); [Testbed Properties - Commands](../testbed-properties/testbed-properties-commands.md); [Puma Errors](puma-errors.md)
