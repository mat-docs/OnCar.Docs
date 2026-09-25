# Data Wizard - Compare

The contents of the Candidate Data Version window are automatically compared with the current Data Version when:

- the Candidate Data Version window is first opened
- the Parameter Mask is changed
- the selected parameters are changed
- a new Data Version is opened

The contents of the Report View window are automatically compared with the Edit Buffer when:

- the Report View window is first opened
- the Parameter Mask is changed
- the selected parameters are changed

The windows are not automatically updated if the Data Version in the Edit Buffer is changed. To force an update, select **DataWizard** > **Compare** or **Compare All**:

- **Compare** - Compares all parameters again between the current Data Version and the Candidate Data Version(s) or the Edit Buffer. The selected parameters and the Parameter Mask are not changed.
- **Compare All** - Compares all parameters again and adds all parameters to the window, but shows only those which differ. The selected parameters and the Parameter Mask are reset to their default values before the comparison.

**See also:** [Data Wizard](index.md); [Data Wizard - Merge](data-wizard-merge.md); [Edit Buffer](../developing-data-versions/index.md)
