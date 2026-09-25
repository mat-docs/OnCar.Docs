# Dial Gauge Display

The Dial Gauge display shows the value of a single Measurement Parameter as a needle on a dial.

To create a Dial Gauge Window, select **Desktop** > **Window** > **Dial Gauge** (Alt+Shift+U), then drag a Measurement Parameter into it from the Parameter Explorer or paste one in. A Dial Gauge Window holds only one Parameter.

## Features

- Markers are drawn round the dial with their values. Markers below the Parameter's Low warning limit are drawn in the **Limit warning 2** colour and markers above the High warning limit in the **Limit warning 1** colour; the warning ranges are also marked on the dial.
- The needle is drawn in the **Needle** colour. The colours are set in the [Display](../using-system-monitor/windows/using-windows/window-properties-display-tab.md) tab of the Window Properties dialog box.
- A label can be shown on the dial face.

## Dial tab

Use the **Dial** tab of the Window Properties dialog box to set the scale:

| Control | Description |
|---|---|
| **Min Value** / **Max Value** | The values at the ends of the dial. Default: the Lower and Upper Engineering Limits of the Parameter (set in the Conversion tab of the Parameter Properties dialog box). |
| **Number of Markers** | The number of markers round the dial. Default 20. |
| **Sweep Angle** | The angle of the dial in degrees. Default 270. |
| **Values Format** | The format of the marker values. Default: the format of the Parameter. |
| **Label** | Text shown on the dial face. Default: the units of the Parameter. |

Other controls for the customisation of the Window are on the [Display](../using-system-monitor/windows/using-windows/window-properties-display-tab.md) tab of the Window Properties dialog box and on the Window System Menu.

**See also:** [Data Display](index.md); [Measurement Parameters](../using-system-monitor/parameters/measurement-parameters.md)
