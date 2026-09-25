# PCU Dash Config Window

The PCU Dash Configuration window is used to lay out the display and download it to the PCU-400 Display Unit. The window is an accurate representation of the display unit, including its shift lights, alarm lights and push switches. Displays are created by dragging Parameters from the Parameter Explorer onto the display area and then choosing how to display the Parameter data, for example numerically or as a Bar Graph or Rev Bar.

![PCU Dash Configuration window](assets/pcu-dashboard-config-window.gif)

Only one PCU Dash Configuration window can be open at a time.

**To open the PCU Dash Configuration window:**

1. Select **Desktop** > **Window** > **Dashboard**.

The window opens with one blank page, **Page 1**. Further pages can be added as required. The command is only available for PCU-400 projects; see [Requirements](../requirements.md).

## Features

### Drag and drop Parameters

Measurement Parameters are dragged from the Parameter Explorer onto the display area. The Parameter name, value and units are shown by default in a Numeric Control.

### Control types

Parameter data can be displayed as a [Numeric](display-control-types/numeric-control.md), [Bar Graph](display-control-types/bar-graph-control.md), [Rev Bar](display-control-types/rev-bar-control.md), [Dial](display-control-types/dial-control.md) or [LED](display-control-types/led-control.md) Control. To change the type, select the Control and choose a different type from the [Context menu](pcu-context-menus.md). Text-only [Static Labels](display-control-types/static-labels.md) and Conditional Text controls can also be added.

### Size and move Controls

Controls can be sized and moved anywhere in the display area. See [Size and Move Display Controls](display-control-types/size-and-move-display-controls.md). **Undo Last Move/Resize** (Ctrl+Z) reverses the last change.

### Display grid

A grid can be superimposed on the display area so that Controls can be aligned with the **Snap To Grid** commands. See [Dash Properties - Layout](pcu-dash-properties/layout-tab.md). The grid is not shown on the display unit when the configuration is downloaded.

### Pages

A new configuration has a single page. Pages can be added, deleted, renamed and reordered from the Page Bar context menu. Click a page tab on the Page Bar to view that page.

### Copy and paste

Controls can be copied and pasted onto the same page or onto a different page.

### Zoom

The display area can be shown at 1, 1.5 or 2 times its normal size using **Zoom Dashboard** on the [Main Menu](dash-configuration-main-menu.md).

### Menus

The [Main Menu](dash-configuration-main-menu.md) is opened from the icon at the left of the window's title bar. Further commands are available on the [Context menus](pcu-context-menus.md).

### Shift lights

The PCU-400 shift lights are configured on the [Shift Lights](pcu-dash-properties/shift-lights-tab.md) tab of the PCU Dash Properties dialog box.

### Actions

Actions are associated with a Parameter and perform an action, for example Flash All LEDs, when their Primary and Secondary conditions are met. See [Dash Properties - Actions](pcu-dash-properties/actions-tab.md).

### Import and export

Configurations (.pcu) and single pages (.ppc) can be exported and imported. See [Import and Export the config](import-and-export-the-config.md).

**See also:** [Create a PCU Dash Configuration](../create-a-pcu-dashboard-config.md)
