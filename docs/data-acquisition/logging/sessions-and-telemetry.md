# Sessions and Telemetry

A Session is the data obtained during a test or a race. Sessions can be generated in the following ways:

| Method | Description |
|---|---|
| **Live** | If the ECU is On-Line (in a testbed situation for example), System Monitor can record a Session file (.ssn) suitable for analysis by [ATLAS](../../technical-support/atlas.md). The characteristics of the Session file are set using the [Live Logging](live-logging/index.md) configuration. |
| **Upload** | If Data Logging is used, System Monitor configures the ECU to choose the parameters to be included in the session as well as the trigger and sample rate characteristics. See [Logging Memory Allocation](logging-memory-allocation.md). System Monitor does not have any direct involvement in generating these Session files. They are created by uploading the data from the ECU into [ATLAS](../../technical-support/atlas.md). |
| **Telemetry** | Data is transmitted from a moving vehicle during the test session. System Monitor does not have any direct involvement in generating the Session files. [ATLAS](../../technical-support/atlas.md) receives the data and analyses it live, and generates a Session file when Telemetry stops. |

TAGtronic systems support two types of telemetry:

- **Narrow Band (Continuous)** - Low data rate telemetry that sends data continuously using low frequency radio. System Monitor is not used to configure this type of telemetry.
- **Wide Band (Burst)** - High data rate telemetry that sends data in bursts using high frequency (microwave) radio. Data is logged into the [Burst Memory](logging-memory-allocation.md), the contents of which are transmitted in each burst. System Monitor configures this type of telemetry using the [Burst Logging](burst-logging/index.md) configuration.

On units that support it, Remote Logging channels can also be sent by telemetry (see the **Telemetry** option in [Channel Properties and Configuration](remote-logging/configure-remote-logging-dialog-box/channel-properties-and-configuration.md)).
