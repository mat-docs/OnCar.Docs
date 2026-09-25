# ECU Files

ECU files are the embedded software files for the ECU, distributed by the [customer support team](../../../technical-support/technical-support.md) or by the ECU manufacturer. They are not part of System Monitor.

The type of ECU and your application determine which of the following files are supplied:

| File | Extension | Required? |
|---|---|---|
| **ASAP2 File** | .a2l | Required by System Monitor |
| **Hex File** | .hex | Required by System Monitor |
| **Controllers File** | .ini | Required by System Monitor |
| **Errors File** | .ini | Optional |
| **Events File** | .ini | Optional |
| **Adjustment Parameters** | .ini | Optional |
| **Sensors File** | .ini | Optional |
| **Sensor Injector File** | .ini | Optional |
| **Sensor Enable/Disable File** | .ini | Optional |
| **Live AutoTune File** | .ini | Optional |

See [Creating a Program Version](../../program-and-data-versions/creating-a-program-version.md) for more details.

The ASAP2 file contains:

- A customer reference and the ECU type for security (the [ASAP](../../asap-compatibility.md) project name).
- A version number, which is used to define the Program Version name and the directory for all the data files based on this ASAP file.
- The name of each [Measurement Parameter](../../../using-system-monitor/parameters/measurement-parameters.md), plus the [Parameter Properties](../../../using-system-monitor/parameters/parameter-properties/index.md) found on the [General](../../../using-system-monitor/parameters/parameter-properties/general-tab.md), [Measurement](../../../using-system-monitor/parameters/parameter-properties/measurement-tab.md) and [Conversion](../../../using-system-monitor/parameters/parameter-properties/conversion-tab.md) tabs.
- The name of each [Editable Parameter](../../../using-system-monitor/parameters/editable-parameters.md), plus all of the Parameter Properties including [Axis Properties](../../../using-system-monitor/parameters/parameter-properties/axis-properties/index.md).
- The names of the [Parameter Groups](../../../using-system-monitor/parameters/names-descriptions-and-groups.md).
- All of the [Conversion](../../../using-system-monitor/parameters/parameter-properties/conversions/conversion-properties.md) formulae.
- Information about the memory locations of each ECU controller (see [ECU Memory](../../../ecu-control/ecu-memory/index.md)).
- Information about the memory location of each parameter value in an ECU controller data area.

The Hex file contains:

- The program code for each ECU controller.
- The configuration for each controller. This includes a revision number, a date stamp, a data version stamp, and the size and memory location of the data used by each controller.
- The data for each controller. The data in each data area forms the base set of parameter values for the ECU.

The Controllers file contains:

- A list of all controllers in the ECU, plus any external controllers connected (for example, the PCU driver's display).
- A name and number for each controller, used by System Monitor for identification.
- An ident number for each controller, for reference to the controller information in the ASAP file.
- A set of properties for each controller.

The Sensors file contains:

- A list of all available sensor types.
- A list of the sensors chosen for use with this ECU.
- Information for the ECU controllers defining the memory size and location of the sensor data.

The Sensor Enable/Disable file contains:

- A list of sensors which can be enabled and disabled by the ECU.

The Live AutoTune file is used by [Live Auto Tune](../../../tuning/live-auto-tune.md).

!!! note
    The sensor calibration (.prm) file, which lists the ASCII calibration data files for the sensors used, is no longer part of the Program Version. It is set for System Monitor as a whole with the Advanced Setting **File for sensor calibration**. See [Calibration Files](../../../data-acquisition/sensors/software-calibrated-sensors/calibration-files.md). The [customer support team](../../../technical-support/technical-support.md) will usually set up your PC for sensor calibration.

**See also:** [Files](../index.md); [Program and Data Version Files](program-and-data-version-files.md)
