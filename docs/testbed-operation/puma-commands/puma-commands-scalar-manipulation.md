# Puma Commands - Scalar Manipulation

The Scalar commands are available only in **Full-operation** mode. In Measurement mode they receive a *command not available* reply.

| System Monitor command | PUMA command | Function |
|---|---|---|
| Get Scalar from System Monitor | Get Parameter from AP-S | PUMA sends: <br>- a LUN (must always be 1) <br>- a parameter identifier. <br>System Monitor returns: <br>- the value of the scalar <br>- the minimum plausible physical limit for the value <br>- the maximum plausible physical limit for the value <br>- the minimum increment. <br>If the parameter is not a scalar editable parameter in the Project's system description, System Monitor replies with an *error during execution* [Error Message](puma-errors.md) ("Invalid parameter"). <br>This command cannot be used to obtain the value of a measurement parameter. |
| Set Scalar on System Monitor | Set Parameter on AP-S | PUMA sends: <br>- a LUN (must always be 1) <br>- a parameter identifier <br>- a value. <br>System Monitor sets the value in the Edit Buffer. If Live Tune is on (see **Switch Offline/Online**), the change is downloaded to the ECU. <br>If the parameter is not a scalar editable parameter in the Project's system description, System Monitor replies with an *error during execution* [Error Message](puma-errors.md) ("Invalid parameter"). <br>If the value is outside its limits, it is capped. System Monitor does not send an error message. |

**See also:** [Puma Commands - Data Acquisition](puma-commands-data-acquisition.md)
