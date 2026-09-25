# Tuning

Tuning is the process of optimising the performance of a vehicle by changing the values of Editable Parameters.

Tuning can be:

- **Off-line** - The changed values of the Editable Parameters are saved in a new Data Version and the changes are sent to the ECU at another time (see [Data Changes in the ECU](../ecu-control/data-changes-in-the-ecu/index.md)). The ECU does not have to be connected to System Monitor while the changes are being made, only while they are downloaded.
- **On-line** - The ECU is connected to System Monitor while the values of the Editable Parameters are being changed. The updated values may be sent to the ECU immediately (using [Live Tune](live-tune.md)) or on demand (**ECU** > **Download Data Changes**).
- **Automatic** - System Monitor can operate in conjunction with an automatic [Testbed](../testbed-operation/index.md) to tune an engine unattended. The AVL PUMA protocol is supported.

To make it easier to adjust values, an [Adjustment Board](../hardware/adjustment-board.md) can be connected to System Monitor. See [Adjustment Board Control](adjustment-board-control/adjustment-board-control.md).

**See also:** [Changing Parameter Values](changing-parameter-values/index.md); [Data Display](../data-display/index.md); [Developing Data Versions](../project-management/developing-data-versions/index.md); [ECU Control](../ecu-control/index.md); [Editable Parameters](../using-system-monitor/parameters/editable-parameters.md); [Testbed Operation](../testbed-operation/index.md)
