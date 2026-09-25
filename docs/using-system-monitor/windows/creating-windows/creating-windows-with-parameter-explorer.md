# Creating Windows with Parameter Explorer

To create a new Window directly from Parameter Explorer, do one of the following:

- Select one or more parameters or a [Group](../../parameters/names-descriptions-and-groups.md), then press ENTER.
- Select one or more parameters or a Group, then Copy and Paste using the Edit Menu commands.
- Double-click a single parameter.

The type of Window created depends on the type of Parameter selected:

| Parameter type | Window created |
|---|---|
| Any Measurement Parameter (including Virtual, External Inputs, CAN and input signal parameters) | A [Numeric Window](../../../data-display/numeric-display/numeric.md) displays all the selected parameters. If only one parameter is selected, the Window uses the [Big Number](../../../data-display/numeric-display/big-number.md) style (large font, no Name or Description columns, no column headings). To use a different display method, create an empty Window. |
| Scalar | A [Scalar Window](../../../tuning/scalar-window.md) displays all the selected parameters. |
| 1-axis Map | A [1-axis Map Window](../../../tuning/1-axis-map-window/1-axis-map.md) opens for each selected parameter. If the parameters share a common axis, they are placed in the same Window. |
| 2-axis Map | A [2-axis Map Window](../../../tuning/2-axis-map-window.md) opens for each selected parameter. |
| Array | An [Array Window](../../../tuning/array-window.md) opens for each selected parameter. |
| String | A [String Window](../../../tuning/string-window.md) displays all the selected parameters. |

If you select a Group of parameters for a Numeric or a Scalar Window, the Group Name or Description, or both (depending on what is displayed in Parameter Explorer at the time), is used as the Window title.

Windows cannot be created this way when the current Page is locked.

**See also:** [Groups](../../parameters/names-descriptions-and-groups.md); [Parameter Explorer](../../parameters/parameter-explorer.md); [Editable Parameters](../../parameters/editable-parameters.md); [Measurement Parameters](../../parameters/measurement-parameters.md)
