# Adjustment Board Control

The Adjustment Board (Pot Board) can be used to change parameter values by turning a control knob. Turning a control is the same as [changing the parameter value](../changing-parameter-values/index.md) by one step.

The parameters for each control are assigned in the [Pot Board Configuration](adjustment-board-configuration.md) window. Only Scalar parameters that can be live tuned can be assigned; a control can instead be assigned to the Maths Bar.

A Program Version can also include an **Adjustment Parameters** file (`.ini`), selected when the [Program Version is created](../../project-management/program-and-data-versions/creating-a-program-version.md). Parameters defined in it have an extra **Adjustment** tab in their Parameter Properties, with **Zero value** and **Step** settings. See [Parameter Properties - Adjustment tab](../../using-system-monitor/parameters/parameter-properties/adjustment-tab.md).

The Adjustment Board only changes values while the ECU is On-Line and Live Updates is on.

## Tools > Pot Board menu

| Command | Description |
|---|---|
| **Configure...** (Ctrl+Shift+F1) | Opens the [Pot Board Configuration](adjustment-board-configuration.md) window. |
| **Enable** (Ctrl+Shift+F2) | When checked, the controls on the Adjustment Board are active. If the ECU is not On-Line or Live Updates is off, System Monitor switches them on first; the board is not enabled if this fails. Requires an open Pot Board Config file, and is not available while Live Auto Tune is on. |
| **Reset Adjustments** (Ctrl+Shift+F3) | Restores every parameter assigned in the Pot Board Configuration to its value saved on disk. Only acts while Live Updates is on. |
| **Recent Files** | A list of recently opened Pot Board Config files. |

**See also:** [Adjustment Board](../../hardware/adjustment-board.md); [Adjustment Board Configuration](adjustment-board-configuration.md); [Parameter Properties - Adjustment tab](../../using-system-monitor/parameters/parameter-properties/adjustment-tab.md); [Adjustment Board Keyboard Operation](adjustment-board-keyboard-operation.md); [Pot Board Properties](pot-board-properties.md)
