# Editable Parameters

Editable Parameters (Tune Data) can be modified to optimise some aspect of the vehicle's performance or to set specific conditions within the ECU. These parameters are viewed and edited in Edit Windows.

Any aspect of an ECU that can be changed in System Monitor is made available as an Editable Parameter. The type of Parameter is defined in the ASAP file by the ECU manufacturer. The ASAP file also permits or prevents System Monitor from changing the values of the Parameter.

System Monitor supports the following types of Editable Parameter:

- [Scalar](../../tuning/scalar-window.md) – returns a single fixed value.
- [1-axis Map](../../tuning/1-axis-map-window/1-axis-map.md) – returns a value that depends on the value of a single index. The index may be selected by a Measurement Parameter.
- [2-axis Map](../../tuning/2-axis-map-window.md) – returns a value that depends on the values of two indices. One or both of the indices may be selected by a Measurement Parameter.
- [Array](../../tuning/array-window.md) – returns a value that depends on the value of a single index.
- [String](../../tuning/string-window.md) – returns a fixed text string.

To view and edit the values of an Editable Parameter, the Parameter must be displayed in a Window. Each type of Editable Parameter has a specific type of Window. You can also view and edit Scalar parameters in a Grid window.

Each Parameter has Properties, most of which are defined in the ASAP file by the ECU manufacturer and can be viewed, but not edited, in System Monitor. The remaining properties can be edited.

**See also:** [Adjustment Board Control](../../tuning/adjustment-board-control/adjustment-board-control.md); [ASAP](../../project-management/asap-compatibility.md); [Changing Parameter Values](../../tuning/changing-parameter-values/index.md); [Using System Monitor](../index.md); [Tuning](../../tuning/index.md); [Parameter Properties](parameter-properties/index.md)
