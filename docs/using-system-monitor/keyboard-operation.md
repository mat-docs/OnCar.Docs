# Keyboard Operation

System Monitor supports the keyboard shortcuts below. They are taken from the System Monitor accelerator tables; most are only available when a Project is open. Shortcuts that also work with no Project open are marked \*.

Many menu commands also have keyboard access through the Menu Bar: press ALT, then the underlined letter. See [Menus](menus/index.md).

## Desktop and Windows

| Keys | Action |
|---|---|
| F1 | Opens Help for the current task or command. With no Project open \*, opens the Help topics. |
| SHIFT+F1 \* | Context help: click a button, menu or window to get help on it. |
| F5 | Refreshes the active Window (**View** > **Refresh**). |
| F6 / SHIFT+F6 \* | Moves focus to the next / previous pane. |
| PAGE DOWN \* | Moves to the next Page in the Desktop (wraps round to the first Page). When Parameter Explorer has focus, scrolls Parameter Explorer instead. |
| PAGE UP \* | Moves to the previous Page in the Desktop (wraps round to the last Page). When Parameter Explorer has focus, scrolls Parameter Explorer instead. |
| ALT+HOME | Moves to the first Page. |
| ALT+END | Moves to the last Page. |
| ALT+PAGE UP | Moves the current Page up one position. |
| ALT+PAGE DOWN | Moves the current Page down one position. |
| ALT+SHIFT+P | Creates a new Page after the current Page. |
| ALT+SHIFT+Z | Zero All Measurements on the current Page. |
| ALT+SHIFT+D | Clear All Display Offsets On Page. |
| ALT+SHIFT+F | Resize Views On Page To Fit Contents. |
| ALT+- | Opens the Window System Menu. |
| ALT+ENTER | Opens the Properties dialog box for the selected Window or Parameter Explorer item. |
| CTRL+E | Toggles Appear on Every Page for the selected Window. |
| ALT+G | Switches a 1-axis or 2-axis Map between grid and graphical display. |
| ALT+Z | Zero All Values in the selected Numeric Window. |
| ALT+D | Clear All Display Offsets in the selected Numeric Window. |
| CTRL+F4 | Closes the selected Window. |
| CTRL+F6 or CTRL+TAB | Moves focus to the next Window on the Page. |
| CTRL+SHIFT+F6 or CTRL+SHIFT+TAB | Moves focus to the previous Window on the Page. |
| SHIFT+F10 | Opens the Context menu for the cursor location. |
| ALT+F4 | Closes the Project and exits System Monitor. |

## Tool and Information Bars

| Keys | Action |
|---|---|
| ALT+0 \* | Shows or hides Parameter Explorer. |
| ALT+1 \* | Shows or hides the Standard Tool Bar. |
| ALT+2 \* | Shows or hides the Page Bar. |
| ALT+3 \* | Shows or hides the ECU Bar. |
| ALT+4 \* | Shows or hides the Maths Bar. |
| ALT+5 \* | Shows or hides the Map Bar. |
| ALT+6 \* | Shows or hides the Comms Bar. |
| ALT+7 \* | Shows or hides the Notes Bar. |
| ALT+8 \* | Shows or hides the Programming Bar. |
| ALT+9 \* | Shows or hides the Extended Comms Bar. |

## Parameter Explorer

| Keys | Action |
|---|---|
| ENTER | Opens the selected Parameters or Group in a new Window. |
| ESC | Moves focus from Parameter Explorer to the active Window. |
| ALT+A | Makes the selected Application the Active Application. |
| CTRL+ALT+N | Toggles Names on and off. |
| CTRL+ALT+D | Toggles Descriptions on and off. |
| CTRL+ALT+G | Toggles Groups on and off. |
| CTRL+SHIFT+G | Creates a new Group. |
| CTRL+SHIFT+V | Creates a Virtual Parameter. |

## Creating Windows

| Keys | Action |
|---|---|
| ALT+SHIFT+S | New Scalar Window. |
| ALT+SHIFT+1 | New 1-axis Map Window. |
| ALT+SHIFT+2 | New 2-axis Map Window. |
| ALT+SHIFT+Y | New Array Window. |
| ALT+SHIFT+R | New String Window. |
| ALT+SHIFT+N | New Numeric Window. |
| ALT+SHIFT+A | New Bar Graph Window. |
| ALT+SHIFT+O | New Oscilloscope Window. |
| ALT+SHIFT+G | New Grid Window. |
| ALT+SHIFT+U | New Dial Gauge Window. |
| ALT+SHIFT+E | New Error Window. |
| ALT+SHIFT+V | New Event Window. |
| ALT+SHIFT+I | New Signal Sampling Window. |
| ALT+R | New Read RAM Window. |

!!! note
    The Desktop > Window menu also shows ALT+SHIFT+B (Big Number), ALT+SHIFT+L (Alarms), ALT+SHIFT+D (Dashboard) and CTRL+SHIFT+F1 (Pot Board), but these keys do not create those Windows. ALT+SHIFT+D clears the display offsets on the Page and CTRL+SHIFT+F1 opens the Pot Board configuration.

## File

| Keys | Action |
|---|---|
| CTRL+N \* | New. |
| CTRL+O \* | Open. |
| CTRL+S | Save. With no Project open \*, Select Base (or Manage Unit.Def Files). |
| ALT+S | Save As. |
| CTRL+SHIFT+S | Save All. |
| CTRL+I \* | Import. |
| CTRL+T | Export Project. |
| CTRL+P | Print. |

## Editing

| Keys | Action |
|---|---|
| CTRL+Z or ALT+BACKSPACE \* | Undo. |
| CTRL+Y | Redo. |
| CTRL+X or SHIFT+DELETE \* | Cut. |
| CTRL+C or CTRL+INSERT \* | Copy. |
| CTRL+V or SHIFT+INSERT \* | Paste. |
| CTRL+ALT+V | Paste Special. See [Edit Menu](menus/edit-menu.md). |
| CTRL+A \* | Select All. |
| F2 | Restore Value: replaces the value with the value from the current Data Version. Editable Parameters only. |
| DELETE | Deletes the selected item. |

## Maths Bar

| Keys | Action |
|---|---|
| ALT+= | Equals: replaces the selected values with the constant. |
| ALT+UP ARROW | Adds the constant. |
| ALT+DOWN ARROW | Subtracts the constant. |
| ALT+RIGHT ARROW | Multiplies by the constant. |
| ALT+LEFT ARROW | Divides by the constant. |

See [Maths Bar](tool-and-information-bars/maths-bar.md).

## ECU control

| Keys | Action |
|---|---|
| F3 | Toggles the ECU On-Line and Off-Line. See [ECU On-Line](../ecu-control/ecu-on-line.md). |
| F4 | Toggles Live Updates on and off. See [Live Tune](../tuning/live-tune.md). |
| ALT+F3 | Live Auto Tune. See [Live Auto Tune](../tuning/live-auto-tune.md). |
| F7 | Download Data Changes. See [Data Changes in the ECU](../ecu-control/data-changes-in-the-ecu/index.md). |
| ALT+F7 | Upload Data. |
| F8 | Delete Errors. |
| F9 | Clear Events. |
| F10 | Save Auto Tune Adjustment. |
| F11 | Delete Min/Max. |
| F12 | Set System Time and Date. |
| ALT+P | Reprogram Unit. |
| CTRL+ALT+P | Reprogram All. |
| ALT+C | Force Complete Reprogram. |
| ALT+K | Kill Engine. |
| ALT+M | Opens the Single Message dialog box. |
| CTRL+U | Opens the Unit Status dialog box. |
| CTRL+Q | Matlab Import. |

## Logging

| Keys | Action |
|---|---|
| CTRL+F1 | Burst Configuration. |
| CTRL+F2 | Burst Download. |
| CTRL+ALT+F2 | Burst Upload. |
| CTRL+F3 | Burst Reset. |
| CTRL+F5 | Remote Configuration. |
| CTRL+ALT+F5 | Remote Download. |
| CTRL+ALT+F6 | Remote Upload. |
| CTRL+ALT+F7 | Remote New Session. |
| CTRL+F7 | Remote Reset. |
| CTRL+F6 | Remote Configuration Compare. |
| CTRL+F8 | CAN Configuration. |
| CTRL+F9 | CAN Configuration Compare. |
| CTRL+L | Live Configuration. |
| CTRL+ALT+SHIFT+P | Input Signal Sample Entire Page. |
| CTRL+ALT+SHIFT+D | Sample Entire Display (in a Signal Sampling Window). |
| CTRL+ALT+SHIFT+S | Sample Selected Only (in a Signal Sampling Window). |

## Sensors

| Keys | Action |
|---|---|
| CTRL+F11 | Open Sensor Set. |
| CTRL+F12 | Sensor Set Download. See [Sensor Sets](../data-acquisition/sensors/sensors-and-actuators/sensor-sets.md). |
| CTRL+ALT+F12 | Sensor Set Upload. |
| CTRL+SHIFT+F8 | Live Calibration (Sensor Calibration Tool). |
| CTRL+B | External Inputs Configuration. |
| CTRL+F10 | External Inputs Download. See [Loading Configurations](../data-acquisition/logging/loading-configurations.md). |
| CTRL+ALT+F10 | External Inputs Upload. |

!!! note
    The Sensors menu shows CTRL+F8 for Live Calibration and CTRL+F9 for External Inputs Configuration, but those keys run CAN Configuration and CAN Configuration Compare.

## Adjustment Board (Pot Board)

| Keys | Action |
|---|---|
| CTRL+SHIFT+F1 or CTRL+D | Opens the Pot Board configuration. See [Adjustment Board Control](../tuning/adjustment-board-control/adjustment-board-control.md). |
| CTRL+SHIFT+F2 or CTRL+SHIFT+D | Enables or disables the Pot Board. |
| CTRL+SHIFT+F3 | Reset Adjustments. |
| CTRL+1 to CTRL+4 | Moves switch 1 of Pot 1 to 4 to the right. |
| CTRL+5 to CTRL+8 | Moves switch 2 of Pot 1 to 4 to the right. |
| CTRL+SHIFT+1 to CTRL+SHIFT+8 | As CTRL+1 to CTRL+8, but to the left. |

## Testbed

| Keys | Action |
|---|---|
| CTRL+SHIFT+F5 | Opens the Testbed configuration. |
| CTRL+SHIFT+F6 | Enables or disables the Testbed Link. |
| CTRL+SHIFT+F7 | Opens the Testbed Message Window. |

## Dashboard

In a [Dashboard](../pcu-dashboard-configuration/pcu-400-display-unit.md) Window:

| Keys | Action |
|---|---|
| CTRL+PAGE UP / CTRL+PAGE DOWN | Moves the dashboard page up / down. |
| CTRL+Z | Undo Last Move/Resize. |
| DELETE | Deletes the selected control. |

## Macros

| Keys | Action |
|---|---|
| CTRL+M \* | Opens the [Macros](../developer-functions/productivity-tools/macros.md) dialog box. |
| F2 | Stops recording a macro. |
| CTRL+ESC | Stops macro playback. |

**See also:** [Menus](menus/index.md); [Context Menus](menus/context-menus/index.md)
