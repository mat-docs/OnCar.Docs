# Min/Max Statistics

Measurement Parameters are typically the output of a sensor, but some are the results of calculations within the ECU.

An ECU may hold minimum and maximum values of a parameter, which can also be read out as Measurement Parameters. System Monitor can reset these minimum and maximum values.

**ECU** > **Delete Min/Max** (F11) sends a signal to the ECU to delete all its min/max data. The command is only available if the Customer Base permits it (**Permit delete errors** in [Customer Base Advanced Settings](../../project-management/customer-bases/customer-base-advanced-settings.md)).

The command is applied to the Active Applications only.

**See also:** [ECU Control](../index.md); [Measurement Parameters](../../using-system-monitor/parameters/measurement-parameters.md)
