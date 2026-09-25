# Parameter Properties

Each Parameter has a set of properties. Most of them are defined by the ECU manufacturer in the ASAP file and are read only in the Parameter Properties dialog box. However, the ASAP file can be modified to make the properties of a Measurement Parameter editable in System Monitor.

The properties on the Display tab, and most of the properties of a Virtual Parameter, can be edited in System Monitor.

The Parameter Properties dialog box opens for one Parameter at a time. To open it:

- With a Parameter selected in Parameter Explorer, do one of the following:
    - select **Properties** from the Parameter Explorer context menu
    - select **View** > **Properties**
    - press ALT+ENTER
- With a Parameter selected in a Window, select **Properties** from the Window's context menu.
- On the [Parameters](../selecting-parameters/multiple-parameter-selection-window-properties.md) tab of the [Window Properties](../../windows/using-windows/window-properties.md) dialog box for a Window that supports more than one Parameter, either select the Parameter and click **Properties**, or double-click the Parameter.
- On the [Parameter](../selecting-parameters/single-parameter-selection-window-properties.md) tab of the Window Properties dialog box for a Window that supports only one Parameter, click **Properties**.

The parameter name is shown in the title bar. The dialog box has a number of tabs. Some are common to all types of Parameter and some are specific to a type of Parameter. The tabs shown for each type of Parameter are:

| Parameter type | Parameter Properties tabs |
|---|---|
| **Measurement** | General, Measurement, Conversion, Display |
| **Virtual** | General, Measurement, Virtual, Conversion, Display |
| **Scalar** | General, Editable, Conversion |
| **1-axis Map** | General, Editable, 1-Axis Map, Conversion |
| **2-axis Map** | General, Editable, 2-Axis Map, Conversion |
| **Array** | General, Editable, Array, Conversion |
| **String** | General, Editable, String, Conversion |
| **Live Auto Tune** | General, Live Auto Tune |

If a Measurement (ECU) or Scalar parameter is used as an Adjustment Parameter, an [Adjustment](adjustment-tab.md) tab is added before the Conversion tab.

The properties of a locked parameter cannot be displayed by users with restricted access. See [Locked Parameters](../locked-parameters/locked-parameters.md).

**See also:** [Parameters](../index.md); [Parameter Explorer](../parameter-explorer.md); [Windows](../../windows/index.md)
