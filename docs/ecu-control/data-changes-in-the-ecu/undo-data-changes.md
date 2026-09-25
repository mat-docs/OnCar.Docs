# Undo Data Changes

Data changes can be undone with the following ECU menu commands. They act on the Active Applications.

| Command | Action |
|---|---|
| **Undo Data Changes in Unit** | Resets the tune buffers in the unit to the Data Version with which it was programmed (see [Copy ROM to RAM](../ecu-memory/copy-rom-to-ram.md)). Changes in the Edit Buffer are not undone. Not available while Live Updates is on or when **ECU read only mode** is set in Advanced Settings. |
| **Undo Data Changes in Unit & Edit Buffer** | Resets the tune buffers in the unit and the Edit Buffer to the saved Data Version with which the unit was programmed. The unit must contain the same Program and Data Version as the saved file. See [Reset ROM](reset-rom.md). |
| **Undo Data Changes in Edit Buffer** | Resets the Edit Buffer to the saved Data Version. Changes downloaded to the unit are not undone. Does not need a connection to the unit; not available while Live Updates is on. |

!!! note
    These commands can only undo changes made since the Data Version was last saved.

**See also:** [Data Changes in the ECU](index.md); [Reset ROM](reset-rom.md)
