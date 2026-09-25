# ECU On-Line

The ECU must be On-Line to:

- Display or log Measurement Parameters as defined by the Live Logging Configuration.
- Respond to changes in Editable Parameters during Live Tune.
- Operate with a Testbed.

The ECU can only be On-Line if the link to System Monitor is OK. The link status is shown on the [Comms Bar](../using-system-monitor/tool-and-information-bars/comms-bar.md).

![Comms Bar](assets/comms-bar.png)

Select **ECU** > **On Line** (F3) to toggle the ECU between on-line and off-line. The command can be selected even if the link is not OK; the ECU is put on-line as soon as the link is detected. You cannot go off-line while [Live Auto Tune](../tuning/live-auto-tune.md) is on.

The time for which System Monitor tries to send a command message is set by **Timeout before link lost (ms)** in [Advanced Settings](../using-system-monitor/settings.md).

!!! note
    System Monitor can go On-Line whenever a project is opened: set **Go online when opening project (Y/N)** to **Y** in Advanced Settings.

## When the ECU is On-Line

- The Comms Bar shows **Monitor ON**.
- If **Warn if Program Versions do not match (Y/N)** is set to **Y** in Advanced Settings, the Program Version is read from each Active Application in the ECU. If it does not match the Program Version in the Edit Buffer, a message offers:
    - **Sync SM to Unit** - Changes the project's Program Version / Data Version to match the unit, then uploads all the data from the unit into the Edit Buffer.
    - **Reprogram** - Reprograms the controllers whose code or data differs, then goes On-Line.
    - **Force Complete Reprogram** - Reprograms all controllers, then goes On-Line.
    - **Ignore** - Leaves the ECU unchanged and goes On-Line with the mismatch.
    - **Cancel** - The ECU stays Off-line.

!!! note
    **Warn if Program Versions do not match** defaults to **N**. With **N**, the check is not made and the ECU goes On-Line without user intervention.

## When the ECU is Off-Line

- The Comms Bar shows **Monitor OFF**.
- Acquisition of data stops and the most recent values are frozen in the Measurement windows.
- Recording of data to disk stops.
- The Testbed link is disabled.

**See also:** [Advanced Settings](../using-system-monitor/settings.md); [ECU Control](index.md); [Editable Parameters](../using-system-monitor/parameters/editable-parameters.md); [Live Logging Configuration](../data-acquisition/logging/live-logging/index.md); [Measurement Parameters](../using-system-monitor/parameters/measurement-parameters.md); [Live Tune](../tuning/live-tune.md)
