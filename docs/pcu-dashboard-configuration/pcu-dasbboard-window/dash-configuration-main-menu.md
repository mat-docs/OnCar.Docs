# Dash Configuration Main Menu

The Main Menu contains commands for the Dash Configuration as well as the standard Window commands.

To open the Main Menu, click the icon at the left of the PCU Dash Configuration window's title bar, or press Alt+- (hyphen).

For a description of the standard Window commands, see [Window System Menu](../../using-system-monitor/menus/window-system-menu.md).

| Command | Description |
|---|---|
| **Download Config** | Downloads the current configuration to the PCU-400 Display Unit, after asking you to confirm. This overwrites the configuration currently held on the display unit. The command is only available while System Monitor is communicating with the car. If System Monitor is online, it goes offline for the download and then back online. |
| **Export Config...** | Exports the whole Dash Configuration to a .pcu file. See [Import and Export the config](import-and-export-the-config.md). |
| **Import Config...** | Imports a .pcu file. The imported configuration replaces the one currently shown in the window. |
| **Export Current Page...** | Exports the page currently in view to a .ppc file. |
| **Import Page...** | Imports a .ppc file. The imported page is added after the existing pages. |
| **Copy** (Ctrl+C) | Copies the selected Control to the clipboard. |
| **Paste** (Ctrl+V) | Pastes the Control on the clipboard onto the current page. |
| **Undo Last Move/Resize** (Ctrl+Z) | Undoes the last move or resize on the current page. |
| **Appear on Every Page** (Ctrl+E) | When selected, the PCU Dash Configuration window appears on every page of the System Monitor Desktop. |
| **Dash Properties...** (Alt+Enter) | Opens the [PCU Dash Properties](pcu-dash-properties/index.md) dialog box. |
| **Zoom Dashboard** | Shows the display area at **1**, **1.5** or **2** times its normal size. The current zoom level is ticked. |

!!! note
    If the download fails, System Monitor reports "Download failed after multiple retries!".
