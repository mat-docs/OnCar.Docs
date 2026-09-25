# Measurement Parameters

Any item of data that can be reported by the ECU is available in the form of a Measurement Parameter. All Measurement Parameters are treated the same in System Monitor, but they can be grouped according to their source.

Typical sources are:

- ECU parameters
- Adjustment parameters (used to define the [Adjustment Board](../../hardware/adjustment-board.md) control)
- CAN parameters
- TSB ([TAG Sensor Bus](../../hardware/sensor-bus.md)) and External Inputs parameters
- [Virtual Parameters](virtual-parameters/index.md)

Each Parameter has Properties, most of which are defined in the ASAP file by the ECU manufacturer and can be viewed, but not edited, in System Monitor. The remaining properties can be edited.

Measurement Parameters are typically the output of a sensor, but some are the results of calculation within the ECU (see [Min/Max Statistics](../../ecu-control/ecu-memory/min-max-statistics.md)).

**See also:** [Data Display](../../data-display/index.md); [Min/Max Statistics](../../ecu-control/ecu-memory/min-max-statistics.md); [Parameter Properties](parameter-properties/index.md); [Sensor](../../data-acquisition/sensors/index.md); [Virtual Parameters](virtual-parameters/index.md)
