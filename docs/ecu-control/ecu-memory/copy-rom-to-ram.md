# Copy ROM to RAM

Copy ROM to RAM is now the **ECU** > **Undo Data Changes in Unit** command. It sends a signal to the ECU to copy the Data Version from ROM to RAM, which resets all tune buffers in the unit to the Data Version with which it was programmed. The Edit Buffer is not changed.

- The command only acts on the Active Applications.
- It can be used even if the unit has a different Program or Data Version from System Monitor.
- It is not available while Live Updates is on, or when **ECU read only mode** is set to **Y** in Advanced Settings.

To reset the Edit Buffer as well, use **Undo Data Changes in Unit & Edit Buffer** (see [Reset ROM](../data-changes-in-the-ecu/reset-rom.md)).

The [ECU Bar](../../using-system-monitor/tool-and-information-bars/ecu-bar.md) shows the software versions in each application.

**See also:** [ECU Control](../index.md); [ECU Memory](index.md); [Undo Data Changes](../data-changes-in-the-ecu/undo-data-changes.md)
