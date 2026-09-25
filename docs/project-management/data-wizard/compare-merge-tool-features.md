# Compare/Merge Tool Features

## Map Compare Window

Values for 1-Axis and 2-Axis maps, for all Data Versions, can be displayed together in a Map Compare Window. This window mimics the look-up table of the selected parameter, but only shows values that have been changed.

To view parameter values in a Map Compare Window, double-click a 1-Axis Map or 2-Axis Map parameter. See [Map Compare Window](map-compare-window.md).

## View Scalar Properties

To view the properties of a scalar in the current Data Version, double-click a scalar in the parameters list. The parameter details are displayed in a Scalar window. The scalar value is shown but cannot be edited.

## Dtv 1 and Dtv 2 lists

Click the browse button (**...**) to select a Data Version. The Data Version path and name are displayed. The drop-down lists show recently compared versions.

!!! note
    If no Dtv 1 or Dtv 2 Data Version is selected, the Dtv 1 box shows the path and name of the last saved version of the Edit Buffer. Its values are displayed to the left of the Memory column.

## Unload

Click **Unload** to close the Dtv 1 or Dtv 2 Data Version and remove it from the display. Unloading Dtv 1 replaces it with the last saved version of the Edit Buffer, even if Dtv 2 is loaded.

## Parameter list

The parameter list shows a superset of all the parameters in the current Data Version and the Dtv 1 and Dtv 2 Data Versions. Difference icons indicate the differences between the parameters in the Memory and those in Dtv 1 and Dtv 2. See [Data Wizard - Parameter Masking](data-wizard-parameter-masking.md).

The context menu of the parameter list includes **Expand Selected**, **Expand All**, **Collapse All**, **Compare View**, **View Edit Buffer**, **View Dtv1**, **View Dtv2**, **Matlab Export** (from the Memory, Dtv1 or Dtv2), **Groups**, **Properties in Edit Buffer** and **Properties in Dtv1**.

## Reset values

Click **Reset** to undo all changes made to the Merge Buffer.

!!! note
    Changes committed from the Merge Buffer to the Edit Buffer cannot be reset.

## Show only where Dtv1 and Dtv2 differ

Select this check box to filter the list to show only parameters that differ between Dtv 1 and Dtv 2.

## Compare with Max/Min Data Versions

For 1-Axis and 2-Axis parameters, the display shows **Max/Min Error** on a red background if any cells in the map or its axes are above or below the specified maximum or minimum values. **Max/Min OK** on a clear background indicates that the parameter is within the specified maximum and minimum values.

Max/Min comparisons are made with the maximum and minimum Data Versions of the Memory Program Version. See [Map Compare Window Features](map-compare-window-features.md).

**See also:** [Compare/Merge Tool](compare-merge-tool.md)
