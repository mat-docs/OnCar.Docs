# Parameter Edit Mode

A single value of an Editable Parameter can be displayed with Edit Mode either on or off.

Entering a new value turns Edit Mode on and the value is overwritten. Edit Mode is also turned on when a single cell is selected with the mouse.

**Edit Mode on:**

- Only the text is highlighted.
- Only one cell can be selected.
- The [Edit Context Menu](../../using-system-monitor/menus/context-menus/edit-context-menu.md) is available.
- If Copy is selected, only the value is sent to the clipboard. Paste and Paste Special can only paste the value as text.

To turn Edit Mode off, press ESC or ENTER.

**Edit Mode off:**

- The whole cell (or row, in Scalar and String windows) is highlighted.
- Blocks of cells can be selected.
- The [Windows Context Menu](../../using-system-monitor/menus/context-menus/windows-context-menu.md) is available.
- If Copy is selected, the value plus a reference to the original parameter is copied to the clipboard. All Paste and Paste Special options can be used.

Pressing a cursor key while a cell is in Edit Mode selects the next cell in the direction of the arrow, with Edit Mode off.

If multiple values are selected, Edit Mode is always off. Entering a number overwrites the first (top left) of the selected values.

**See also:** [Changing Parameter Values](index.md)
