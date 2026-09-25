# Virtual Parameters Import/Export

Virtual Parameters can be imported and exported as `.vpx` [XML files](virtual-parameters-xml-file-schema.md) from [Parameter Explorer](../parameter-explorer.md).

## Export

1. In Parameter Explorer, select the Virtual Parameters, or the group of Virtual Parameters, that you want to export.
2. Right-click and select **Virtual Parameter Export**.
3. In the Virtual Parameter Export dialog box, enter a file name (the default is *Virtual Parameters - ProjectName*`.vpx`) and click **Save**.

Conversions defined specifically for Virtual Parameters are also exported.

All Virtual Parameters that depend on another Virtual Parameter are exported with it, even if they were not selected for export.

## Import

1. In Parameter Explorer, right-click the Virtual Parameters folder (or a group or Virtual Parameter in it) and select **Virtual Parameter Import**.
2. Select the `.vpx` file and click **Open**.

The Virtual Parameters, conversions and groups defined in the file are merged with the existing ones. If there are problems, the warnings are written to the Warning Log and you are asked whether you want to view it.

**See also:** [Virtual Parameter Files](virtual-parameter-files.md); [Virtual Parameters](index.md)
