# Map Compare Window Features

## Colour coding

- Individual cells are coloured red or blue to show that their value is greater than the maximum or less than the minimum value. The cell is clear if the value is within the specified limits.
- Where the values are within the limits, the values are displayed in red if the Dtv value is higher than the Merge Buffer, or blue if it is lower.

## Display settings

The window inherits the following settings from the Compare/Merge Tool:

- The value display selection (Value or Delta)
- Show only where Dtv1 and Dtv2 differ

These settings can be changed for the window from its context menu, in both Overview and Grid modes: **Show Only Where Dtv's Differ**, **Show Value**, **Show Delta Value From Memory**, **Show Delta % From Memory**, **Show Delta Value From Dtv1**, **Show Delta % From Dtv1**, **Show Delta Value From Dtv2** and **Show Delta % From Dtv2**.

## Cell context menu options

The cell context menu allows you to copy values from the Data Versions to the Merge Buffer (Memory) or to the clipboard. Highlight the cell or cells you want to copy from and select an option:

- **Copy Dtv1** - Copies the Dtv 1 values to the clipboard.
- **Copy Dtv1 to Memory** - Copies the Dtv 1 values to the Merge Buffer.
- **Copy Memory** - Copies the Merge Buffer values to the clipboard.
- **Copy Dtv2** - Copies the Dtv 2 values to the clipboard.
- **Copy Dtv2 to Memory** - Copies the Dtv 2 values to the Merge Buffer.
- **Paste** - Pastes from the clipboard to the Merge Buffer.

## Minimum and Maximum Data Versions

If a minimum and/or maximum Data Version file is available in the Program Version folder, System Monitor uses it in the Compare/Merge Tool to indicate whether minimum or maximum values have been exceeded.

Minimum and maximum Data Version files (.dtv) can also be used as Dtv 1 and Dtv 2 Data Versions in the Compare/Merge Tool.

**Create a Minimum or Maximum Data Version:**

Edit a Data Version and save it in the same folder as the Program Version, using the file names:

- *pppp*MIN.dtv for the minimum Data Version
- *pppp*MAX.dtv for the maximum Data Version

where *pppp* is the name of the Program Version file (without the .pgv extension).

**See also:** [Map Compare Window](map-compare-window.md); [Compare/Merge Tool Features](compare-merge-tool-features.md)
