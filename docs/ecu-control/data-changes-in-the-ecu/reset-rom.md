# Reset ROM

The Reset ROM function resets both the ECU and the Edit Buffer to the Data Version that was programmed into the ECU ROM. In the current ECU menu it is the **Undo Data Changes in Unit & Edit Buffer** command. There is no separate "Reset Data to ROM" command.

The command does the following for each Active Application:

1. Checks that the Program Version and Data Version in the unit's ROM match the saved Data Version file loaded in System Monitor. If they do not match, the message "System Monitor and unit have different program/data versions. Cannot reset SM edit buffer to ROM." is shown and nothing is changed. Reprogram the unit, or save any uploaded data, first.
2. Sends a signal to the ECU to copy the Data Version from ROM to RAM (see [Copy ROM to RAM](../ecu-memory/copy-rom-to-ram.md)). All live tunes in the unit are discarded.
3. Overwrites the Edit Buffer with the saved Data Version file. This is equivalent to restoring all values.

The unit is not reprogrammed.

**See also:** [Undo Data Changes](undo-data-changes.md); [Developing Data Versions](../../project-management/developing-data-versions/index.md); [ECU Control](../index.md)
