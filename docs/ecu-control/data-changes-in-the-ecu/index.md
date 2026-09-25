# Data Changes in the ECU

The changes made during tuning are stored as a Data Version in the Edit Buffer.

Only the Active Applications can be tuned.

The data changes may be transferred to the ECU in one of two ways:

- [Live Tune](../../tuning/live-tune.md) **on** - As soon as an Editable Parameter is changed, the new value is loaded into RAM.
- [Live Tune](../../tuning/live-tune.md) **off** - The changes are sent on demand with **ECU** > **Download Data Changes**. See [Downloading Data to the ECU](downloading-data-to-the-ecu.md).

Data can also be [uploaded from the ECU](uploading-data-from-the-ecu.md), and changes can be [undone](undo-data-changes.md).

!!! note
    The data changes only affect the ECU RAM. To apply the changes to the vehicle systems, the ECU must be operating from RAM. See [Run from RAM](../ecu-memory/run-from-ram.md).

**See also:** [ECU Control](../index.md); [Developing Data Versions](../../project-management/developing-data-versions/index.md); [Live Tune](../../tuning/live-tune.md); [Tuning](../../tuning/index.md)
