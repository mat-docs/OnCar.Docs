# Data Wizard - View Parameter

Data Wizard allows temporary windows to be opened to display the values of selected parameters.

## Context menu

The following context menu options are available for a selected parameter in the Report View and Candidate Data Version windows:

- **View Edit Buffer** - Opens a window showing the value of the selected parameter(s) in the current Data Version (as stored in the Edit Buffer).
- **View this Data Version** - Opens a window showing the value of the selected parameter(s) in the Candidate Data Version of the selected window.
- **View Both** - Opens a window for each of the above options.
- **View Differences** - Opens Print Preview for the selected parameter(s). Only available in a Candidate Data Version window.

The context menu also has **Copy**, **Select All**, **Paste**, **Expand All**, **Collapse All**, **Matlab Export** (from the Memory or the Data Version), **Groups**, **Properties in Edit Buffer** and **Properties in this Data Version**.

## Window features

- If more than one parameter is selected, View windows are opened using the same rules as when [creating windows with the Parameter Explorer](../../using-system-monitor/windows/creating-windows/creating-windows-with-parameter-explorer.md).
- View windows appear on all pages. To avoid confusion, it is advisable to use Data Wizard on a blank Page.
- View windows opened for parameters in the Edit Buffer look the same as windows created in the usual way. The title is the Name and/or Description of the parameter. Values can be edited in these windows.
- View windows opened for parameters in a Candidate Data Version can be identified by the title, which includes the full path name of the Data Version file. Values cannot be edited in these windows. They close automatically when the Candidate Data Version window is closed.
- View windows are not stored as part of the Desktop and are not reloaded if a Project is closed and re-opened.
- Individual View windows can be printed, but are not included if you print a Page.

**See also:** [Creating Windows with Parameter Explorer](../../using-system-monitor/windows/creating-windows/creating-windows-with-parameter-explorer.md); [Data Wizard](index.md); [Printing Data Wizard Windows](../../using-system-monitor/printing/printing-data-wizard-windows.md)
