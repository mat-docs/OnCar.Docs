# Error

Special Measurement Parameters code for errors in the ECU. Each bit of the value of the parameter acts as a flag that indicates an error. The [Error Display](error-display.md) shows the error flags that are currently set on the ECU.

## Features

- Errors (groups, names, descriptions, etc.), and the parameters that indicate them, are defined by the Error file. Error Windows can only be displayed if an Error file is included in the Program Version.
- Errors are not stored by System Monitor; the information is always uploaded from the ECU, which must be [On Line](../../../ecu-control/ecu-on-line.md).
- Errors are displayed in the order in which they occur, and are added to the bottom of the Error Window on each update. If an error occurs more than once, only one error entry is displayed.
- Errors may be Current (occurring now) or Logged (have occurred in the past). Logged errors are stored in the ECU. The same error can appear as both Current and Logged.
- If an error is no longer Current (the bit in the corresponding measured value is no longer set), it is removed from the Error Window. However, because the ECU stores logged errors, an error that is no longer current automatically appears in the Error Window as Logged.
- If an error is no longer Logged (the bit in the corresponding measured value is no longer set), it is removed from the Error Window.

**See also:** [Error Display](error-display.md); [Error Mask](error-mask.md); [Deleting Errors](deleting-errors.md); [Measurement Parameters](../../../using-system-monitor/parameters/measurement-parameters.md); [Program Version](../../../project-management/program-and-data-versions/index.md)
